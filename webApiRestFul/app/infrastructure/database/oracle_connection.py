"""
Gestión de conexión a Oracle Database
"""
import oracledb
import json
from pathlib import Path
from typing import Optional


class OracleConnection:
    """Encapsula la conexión a Oracle Database"""
    
    def __init__(
        self,
        user: str,
        password: str,
        dsn: str,
        wallet_dir: Optional[str] = None,
        wallet_password: Optional[str] = None
    ):
        """
        Inicializa la conexión a Oracle
        
        Args:
            user: Usuario de base de datos
            password: Contraseña
            dsn: Data Source Name (servicio)
            wallet_dir: Directorio del wallet (para Autonomous DB)
            wallet_password: Contraseña del wallet (opcional)
        """
        self.user = user
        self.password = password
        self.dsn = dsn
        self.wallet_dir = wallet_dir
        self.wallet_password = wallet_password
        
        # Configurar cliente Oracle si se usa wallet
        if wallet_dir:
            try:
                oracledb.init_oracle_client(config_dir=wallet_dir)
            except Exception as e:
                # Si ya está inicializado, ignorar el error
                pass
    
    def get_connection(self) -> oracledb.Connection:
        """
        Obtiene una conexión a la base de datos
        
        Returns:
            Conexión activa a Oracle
        """
        try:
            if self.wallet_dir:
                # Conexión con Autonomous Database
                connection = oracledb.connect(
                    user=self.user,
                    password=self.password,
                    dsn=self.dsn,
                    config_dir=self.wallet_dir
                )
            else:
                # Conexión simple
                connection = oracledb.connect(
                    user=self.user,
                    password=self.password,
                    dsn=self.dsn
                )
            
            return connection
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"Error de conexión a Oracle: {error.message}")
            raise
    
    def test_connection(self) -> bool:
        """
        Prueba la conexión a la base de datos
        
        Returns:
            True si la conexión es exitosa, False en caso contrario
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 'Connection OK' FROM DUAL")
                result = cursor.fetchone()
                print(f"Prueba de conexión: {result[0]}")
                return True
        except Exception as e:
            print(f"Error en prueba de conexión: {e}")
            return False
    
    @classmethod
    def from_settings_file(cls, settings_path: Path) -> 'OracleConnection':
        """
        Factory method para crear conexión desde archivo de configuración
        
        Args:
            settings_path: Ruta al archivo settings.json
            
        Returns:
            Instancia de OracleConnection
        """
        with open(settings_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        oracle_config = config.get('oracle', {})
        
        return cls(
            user=oracle_config['user'],
            password=oracle_config['password'],
            dsn=oracle_config['dsn'],
            wallet_dir=oracle_config.get('wallet_dir'),
            wallet_password=oracle_config.get('wallet_password')
        )
