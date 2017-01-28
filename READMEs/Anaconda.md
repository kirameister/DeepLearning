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

At leat in my zsh environment (I've been using zsh over a decade). For some reason, it seems that zsh automatically checks whether an env var is defined, and outputs an error, even in an if clause as above. My workaround was to update /anaconda/bin/activate as follows: 

```
# Determine the directory containing this script
if [[ -n ${ZSH_VERSION:-} ]]; then
    _SCRIPT_LOCATION=${funcstack[1]}
    _SHELL="zsh"
elif [[ -n ${BASH_VERSION:-""} ]]; then
    _SCRIPT_LOCATION=${BASH_SOURCE[0]}
    _SHELL="bash"
else
    echo "Only bash and zsh are supported!"
    return 1
fi
..
..
if [[ -n ${BASH_VERSION:-} ]] && [[ "$(basename "$0" 2> /dev/null)" == "activate" ]]; then
    (>&2 echo "Error: activate must be sourced. Run 'source activate envname'
..
..
if [[ -n $ZSH_VERSION ]]; then
    rehash
elif [[ -n $BASH_VERSION ]]; then
    hash -r
else
    echo "Only bash and zsh are supported"
    return 1
fi
```

This indeed looks like a dirty hack. But at least it seems to be working fine in my environment (well, at least so far). 

