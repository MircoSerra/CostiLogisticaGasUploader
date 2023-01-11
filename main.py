import costi_logistica_gas as clg
import time
import datetime
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
	@staticmethod
	def on_any_event(event):
		#print(f'event type: {event.event_type}  ShareNetworkMountPoint : {event.src_path}')
		#print('ok')
		clg.update_costi_logistica_gas(ShareNetworkMountPoint + '/Input Book GEFS.xlsx')

if __name__ == "__main__":
	ShareUserName = 'uforecast'
	SharePassword = "'3>~ve3<|wDd&.9B>'"
	ShareNetworkPath = '//192.168.11.63/Condivisa/Clienti/Arvedi/GEFS/Aggiorna\ parametri\ Book'
	ShareNetworkMountPoint = '/mnt/GEFS_Costi_Logistica_GAS/'
	strMountShare = 'mount -t cifs -o username=%s,password=%s,vers=3.0 %s %s' % (ShareUserName, SharePassword, ShareNetworkPath, ShareNetworkMountPoint)
	strUmountShare = 'umount %s' % (ShareNetworkMountPoint)
	#Monto la cartella da cui prelevare i file XML
	if not os.path.ismount(ShareNetworkMountPoint):
		#La cartella non è montata e quindi la monto
		os.system(strMountShare)
	strfile = os.path.join(ShareNetworkMountPoint + '/Input Book GEFS.xlsx')
	if ((datetime.datetime.today().today() - datetime.datetime.fromtimestamp(os.path.getctime(strfile))).total_seconds()) < 60:
		clg.update_costi_logistica_gas(ShareNetworkMountPoint + '/Input Book GEFS.xlsx')
	os.system(strUmountShare)
	#event_handler = MyHandler()
	#observer = Observer()
	#observer.schedule(event_handler, path = ShareNetworkMountPoint, recursive=False)
	#observer.start()
	#print('partito')
	#try:
	#	while True:
	#		time.sleep(1)
	#except KeyboardInterrupt:
	#	observer.stop()
	#observer.join()
