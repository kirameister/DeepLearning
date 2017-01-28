# Anaconda

While I realize Anaconda is a great mechanism to let multiple "modular" environments live at the same time, I had few very minor issues, which I thought worth noting down (mostly for my future reference).

## PATH is not set automatically: /anaconda/bin

Perhaps it's because I've been using zsh, which is (for some reasno) less known than bash. I used GUI installation and chose to let the Anaconda be used by all the users in the machine (I'm using Mac OS X). It took few minutes to figure out where the Anaconda was actually installed. Solving something like following in my `$HOME/.zshrc` solved the problem: 

```
export PATH=/opt/local/bin:/anaconda/bin:$PATH
```

## $BASH_VERSION: parameter not set, when trying to run source activate

This is most likely caused by the lines like following: 

```
if [[ -n $BASH_VERSION ]]; then
    _SCRIPT_LOCATION=${BASH_SOURCE[0]}
    _SHELL="bash"
```

At leat in my zsh environment (I've been using zsh over a decade). For some reason, it seems that zsh automatically 

