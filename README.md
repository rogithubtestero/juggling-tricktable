<a href="http://robinrosenstock.com/juggling/tricktable">
<img align="right" width="100" height="100" src="/static/logo.png">
</a>
<h1 align="center">The <i>ultimate</i> Juggling Tricktable</h1>

> An interactive list/table of juggling tricks as a single-page application, accessible from any internet capable device.



![](/static/overview.png)




# Table of contents

- [Features](#features)
- [How to use](#how-to-use)
    - [Contributing](#contributing)
    - [Downloading](#downloading)
- [Development](#development)
    - [Dependencies](#dependencies)
    - [Local](#local)
    - [Deployment](#deployment)
- [Libraries](#libraries)
- [Support](#support)
- [License](#license)





## Features

* Grid based tricklist
* Clearly arranged informations
* All in one place
* Sortable
* Filterable
* Links to real life videos
* Links to animations, with the help of [gunswap.co](http://gunswap.co)
* Accessible from everywhere and every device (though Javascript must be enabled)
* Easy editing (See [Contributing](#contributing))




## How To Use

No need for an installation. Just go    [here](https://robinrosenstock.com/juggling-tricktable) and use it.

Make use of the filter!


### Contributing

Contributing is especially important for this app. Because there are far too many tricks to clearly lay out in a table all by myself. So I need *your* help, for building the *ultimate* juggling tricktable.

For now, it is not that easy to add a new trick. Follow these steps:

1. Login to github
2. Go to https://github.com/geniusupgrader/juggling-tricktable/blob/master/static/tricktable.json
3. Hit "Edit this file"
4. make your changes (orient yourself on the available entries) -> Propose file changes
5. Hit "Create Pull request"






### Video

When there is a Website with a video explaining/showing the trick just copy the whole website link and paste it into the "video" field in the json editor. But better way is to use an embed-link from the video directly. To find an embed link to the video is different where the video is hosted.

For Youtube use this:

1. Share (to the right of "I-dislike-this-Button")
2. Embed
3. Copy __only__ the embed link, e.g: https://www.youtube.com/embed/JEI1IGE1EsI
4. Paste it into the json editor





### Download







## Development


### Dependencies

#### with pip:

Having [Python](https://www.python.org/) and [pip](https://pypi.org/project/pip/) already installed, Go on with:

```bash
pip install Flask

```

#### OR within [Arch](https://www.archlinux.org/):

```bash
sudo pacman -S python-flask
```

### Local


To clone and run this application, you'll need [git](https://git-scm.com). From your command line clone the repo and execute the coresponding flask commands.

```bash
git clone git@github.com:geniusupgrader/juggling-tricktable.git
cd juggling-tricktable
export FLASK_APP=tricktable.py
flask run
```

Then go to: [127.0.0.1:5000](http://127.0.0.1:5000).


### Deployment

Refer to your hosting service for exact guidance. Here it is shown and demonstrated how to deploy to one of the best hosting services: __[uberspace](https://uberspace.de/)__.
We are using flask as a micro web framework. From [these](https://blog.lucas-hild.de/flask-uberspace) instructions:


```bash
pip3.6 install flask --user
pip3.6 install flup --user
cd ~
git clone git@github.com:geniusupgrader/juggling-tricktable.git
cd fcgi-bin  # change to the fcgi folder
nano tricktable.fcgi
```
Fill tricktable.fcgi with this content:

```python
#!/usr/bin/env python3.6

import sys
sys.path.insert(0, "/home/USERNAME/flaskapplication")
from app import app

from flup.server.fcgi_fork import WSGIServer
WSGIServer(app).run()
```

Then use `.htaccess` for a clean url and redirecting (this comes into your "html" folder):

```
RewriteEngine on
RewriteBase /
RewriteRule juggling-tricktable /fcgi-bin/tricktable.fcgi/
```




For other tutorials (on uberspace) see:

- https://github.com/JonasGroeger/flask-uberspace-quickstart
- https://gist.github.com/dAnjou/2007865
- http://jonasgroeger.de/projekte/blog/projekt-flask-auf-dem-hoster-uberspace-blitzschnell-mit-hubschen-urls-aufsetzen/





## Libraries

This software uses code from several open source packages. Credits to them (referencing repos):

- [flask](https://github.com/pallets/flask)
- [ag-grid](https://github.com/ag-grid/ag-grid)
- [featherlight](https://github.com/noelboss/featherlight)
-  [json-editor](https://github.com/json-editor/json-editor)



__Related__:

- [Android App: Juggling tricktable](https://github.com/amitmerchant1990/markdownify-web) - Android version of the juggling tricktable


## Support




## License

__MIT__. See [LICENSE.md](LICENSE.md)

> <img style="vertical-align: middle;" width="24" src="https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/32/globe.png"> [robinrosenstock.com](https://robinrosenstock.com)<br>
> <img style="vertical-align: middle;" width="24" src="https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/32/github.png"> [github.com/geniusupgrader](https://github.com/geniusupgrader)<br>
