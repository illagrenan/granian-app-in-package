## Setup

```
poetry install
```

## OK

### Command:

```
cd ./tests_app_not_in_package/
poetry run granian --interface asgi test_app.main:app
```

### Output:

```
[INFO] Starting granian (main PID: 167860)
[INFO] Listening at: 127.0.0.1:8000
[INFO] Spawning worker-1 with pid: 171040
Is number correct? False
[WARNING] ASGI Lifespan errored, continuing without Lifespan support
[INFO] Started worker-1
[INFO] Started worker-1 runtime-1
```

## Not OK

### Command:

```
cd ./tests_app_in_package/
poetry run granian --interface asgi test_app.main:app
```

### Output:

```
[INFO] Starting granian (main PID: 177388)
[INFO] Listening at: 127.0.0.1:8000
[INFO] Spawning worker-1 with pid: 177420
Process granian-worker:
Traceback (most recent call last):
  File "C:\Users\***\AppData\Local\pypoetry\Cache\virtualenvs\granian-app-in-package-bSNNtjZN-py3.12\Lib\site-packages\granian\_internal.py", line 40, in load_module
    __import__(module_name)
  File "C:\work\contrib\granian-app-in-package\tests_app_in_package\test_app\main.py", line 4, in <module>
    from test_app.logic import is_number_correct
ModuleNotFoundError: No module named 'test_app'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\***\AppData\Local\Programs\Python\Python312\Lib\multiprocessing\process.py", line 314, in _bootstrap
    self.run()
  File "C:\Users\***\AppData\Local\Programs\Python\Python312\Lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\***\AppData\Local\pypoetry\Cache\virtualenvs\granian-app-in-package-bSNNtjZN-py3.12\Lib\site-packages\granian\server.py", line 169, in _spawn_asgi_worker
    callback = callback_loader()
               ^^^^^^^^^^^^^^^^^
  File "C:\Users\***\AppData\Local\pypoetry\Cache\virtualenvs\granian-app-in-package-bSNNtjZN-py3.12\Lib\site-packages\granian\_internal.py", line 57, in load_target
    module = load_module(path)
             ^^^^^^^^^^^^^^^^^
  File "C:\Users\***\AppData\Local\pypoetry\Cache\virtualenvs\granian-app-in-package-bSNNtjZN-py3.12\Lib\site-packages\granian\_internal.py", line 43, in load_module
    raise RuntimeError(
RuntimeError: While importing 'tests_app_in_package.test_app.main', an ImportError was raised:

Traceback (most recent call last):
  File "C:\Users\***\AppData\Local\pypoetry\Cache\virtualenvs\granian-app-in-package-bSNNtjZN-py3.12\Lib\site-packages\granian\_internal.py", line 40, in load_module
    __import__(module_name)
  File "C:\work\contrib\granian-app-in-package\tests_app_in_package\test_app\main.py", line 4, in <module>
    from test_app.logic import is_number_correct
ModuleNotFoundError: No module named 'test_app'

[ERROR] Unexpected exit from worker-1
[INFO] Shutting down granian
```