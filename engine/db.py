import oracledb
def db_Connect_thinModePool():
    try:
        ConnectionPool=oracledb.create_pool(user="MOVIESTREAM",password="watchS0meMovies#",dsn="(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.ap-mumbai-1.oraclecloud.com))(connect_data=(service_name=ga97be9115f23e9_moviestreamworkshop2_low.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))",min=1,max=5,increment=1)
        print(ConnectionPool)
        return ConnectionPool
    except Exception as e:
        print("DB Error:  {e}")