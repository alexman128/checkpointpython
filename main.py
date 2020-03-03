from services import CSVFile
from app_config import config

if __name__ == '__main__':
    archivo = CSVFile(config['archivo_csv'], {'test1': 1, 'test2': 2}, 'w')
    archivo.write_content()