# Pre-compiled binaries
You don't have to buid this firmware yourself to run it. Download from:

https://github.com/Fri3dCamp/badge-2020/tree/master/firmware

# App development

Connect to your badge 

``` shell
mpremote /dev/ttyUSB0
```

Ctrl+C to stop the current App

Enable REPL as the default App

``` python
BADGE.settings().set('apps.autorun', 'frozen_apps.repl')
BADGE.settings().store()
```

Mount a directory on your computer to the badge using mpremote.

``` shell
mpremote /dev/ttyUSB0 mount <local_directory>
```

This will open a python terminal (REPL) and your `<local_directory>` is in `/remote`

To run your app:

``` python
import <app_name>
```
