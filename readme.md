

developing:
```bash
flask -A app.app:create_app run
```
or 
```bash
python3 run.py
```
or
```bash
./run.py
```
production:
```bash
gunicorn -w 4 'grun:app'
```
