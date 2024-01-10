### Apostila

Rodar o comando abaixo para iniciar a apresentação:

```bash
docker run --name slidev --rm -it \
    --user node \
    -v ${PWD}/slidev:/slidev \
    -p 3030:3030 \
    tangramor/slidev:latest
```


