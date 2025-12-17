"""
Script para actualizar el password hasheado del usuario admin
Ejecutar este script si no tienes SQL*Plus instalado
"""
import oracledb
import hashlib
import os

def hash_password(password: str) -> str:
    """Genera hash SHA-256 de una contraseña"""
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    print("=" * 50)
    print("  FIX: Actualizar Password Admin")
    print("=" * 50)
    print()
    
    # Configuración para Autonomous Database
    wallet_location = r"C:\Users\Walther\Desktop\INACAP\Progra_de_Objetos\proyectoPyQt6\Wallet"
    
    if not os.path.exists(wallet_location):
        print(f"❌ ERROR: Wallet no encontrado en: {wallet_location}")
        return
    
    # Configurar variables de entorno para el Wallet
    os.environ['TNS_ADMIN'] = wallet_location
    
    print(f"✅ Wallet configurado: {wallet_location}")
    
    # Parámetros de conexión
    user = "admin"
    password = "Zayrus189918143"
    dsn = "basedatos699_medium"
    
    print(f"\nConectando a Oracle Database ({dsn})...")
    try:
        # Intentar con modo thick (requiere Oracle Client)
        try:
            oracledb.init_oracle_client(config_dir=wallet_location)
            conn = oracledb.connect(user=user, password=password, dsn=dsn)
            print("✅ Conexión exitosa (thick mode)")
        except:
            # Si falla, usar modo thin
            print("⚠️  Thick mode no disponible, usando thin mode...")
            conn = oracledb.connect(
                user=user,
                password=password,
                dsn=dsn,
                config_dir=wallet_location,
                wallet_location=wallet_location,
                wallet_password=""
            )
            print("✅ Conexión exitosa (thin mode)")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return
    
    try:
        cursor = conn.cursor()
        
        # Hash de las contraseñas
        admin_hash = hash_password("admin123")
        user_hash = hash_password("user123")
        
        print(f"\nHash de 'admin123': {admin_hash}")
        print(f"Hash de 'user123': {user_hash}")
        
        # Actualizar admin
        print("\nActualizando usuario 'admin'...")
        cursor.execute("""
            UPDATE usuario 
            SET password_hash = :hash
            WHERE username = 'admin'
        """, hash=admin_hash)
        
        rows_updated = cursor.rowcount
        if rows_updated > 0:
            print(f"✅ Usuario 'admin' actualizado ({rows_updated} filas)")
        else:
            print("⚠️  Usuario 'admin' no encontrado")
        
        # Actualizar usuario1
        print("\nActualizando usuario 'usuario1'...")
        cursor.execute("""
            UPDATE usuario 
            SET password_hash = :hash
            WHERE username = 'usuario1'
        """, hash=user_hash)
        
        rows_updated = cursor.rowcount
        if rows_updated > 0:
            print(f"✅ Usuario 'usuario1' actualizado ({rows_updated} filas)")
        else:
            print("⚠️  Usuario 'usuario1' no encontrado")
        
        # Commit
        conn.commit()
        print("\n✅ Cambios confirmados (COMMIT)")
        
        # Verificar
        print("\nVerificando usuarios actualizados:")
        cursor.execute("""
            SELECT username, password_hash, nombre_completo, rol 
            FROM usuario 
            WHERE username IN ('admin', 'usuario1')
        """)
        
        for row in cursor:
            print(f"  - {row[0]}: {row[2]} [{row[3]}] - Hash: {row[1][:20]}...")
        
        cursor.close()
        
    except Exception as e:
        print(f"\n❌ Error durante la actualización: {e}")
        conn.rollback()
        print("⚠️  Cambios revertidos (ROLLBACK)")
    finally:
        conn.close()
        print("\n✅ Conexión cerrada")
    
    print("\n" + "=" * 50)
    print("  PASSWORD ACTUALIZADO")
    print("=" * 50)
    print("\nAhora intenta hacer login con:")
    print("  Usuario: admin")
    print("  Password: admin123")
    print()

if __name__ == "__main__":
    main()
    input("\nPresiona ENTER para salir...")
