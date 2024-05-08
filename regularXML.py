import re
import zlib

def extract_streams(file):
    with open(file, 'rb') as f:
        data = f.read()

    block_XML = re.findall(b'stream(.*?)endstream', data, re.DOTALL)

    for i, block in enumerate(block_XML):
        try:
            data = zlib.decompress(block)
            with open(f'stream_{i}.bin', 'wb') as res:
                res.write(data)
            print(f"Блок {i} успешно извлечен и сохранен в файл 'stream_{i}.bin'")
        except zlib.error:
            print(f"Ошибка при распаковке блока {i}")

file = ''
extract_streams(file)