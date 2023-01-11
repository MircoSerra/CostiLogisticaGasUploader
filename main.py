import costi_logistica_gas as clg
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = 'Y:/Clienti/Arvedi/GEFS/Aggiorna parametri Book/'


class MyHandler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        print(f'event type: {event.event_type}  path : {event.src_path}')
        print('ok')
        clg.update_costi_logistica_gas(path + '/Input Book GEFS.xlsx')


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    print('partito')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
