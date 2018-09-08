# Markdown Album Extension

### What the heckbiscuit is this?

This is an extension I made for automatically generating albums in . The HTML generated for the albums uses [fancybox](http://fancybox.net/) and [bootstrap](https://getbootstrap.com/). While not required, they will make your project look really pretty.

Images are specified by `[alt-text](link-to-image.jpg)` fenced in `@@@` and deliniated by `-`. For example:

```
@@@
[](/data/2018/8/1/8b4d24be-139a-4a28-ace3-7f9b78123729.jpeg)-
[](/data/2018/8/1/71f72258-1977-4253-8578-dd338f9f9f7f.jpeg)
@@@
```

To use:

```
from  import AlbumExtension
markdown.markdown(example_text, extensions=[AlbumExtension()])
```
