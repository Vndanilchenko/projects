запустить **docker-compose up** и любоваться тем, как обрабатываются сообщения
- **start faust -a messages_producer worker -l info --web-port 6066** запуск генератора сообщений

- **start faust -A preprocess worker -l info --web-port 6067** - запуск преобработчика сообщений

- **start faust -A reply worker -l info --web-port 6068** - запуск первого генератора ответов

- **start faust -A reply worker -l info --web-port 6069** - запуск второго генератора ответов (т.к. один процесс не справляется с потоком)
