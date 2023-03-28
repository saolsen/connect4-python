# Make it faster.


## before
`scripts/perf.py` before doing any work
* about 9 seconds
### Scalene
* scalene shows 60% of time in `_check`, which evaluates to see if board is winner.
* 12% of time in `deepcopy` of the board when creating random games from existing game.

### Plan
Sort of what I expected. I think with numpy we can speed up the check and the copy.

## switch to numpy
* Just switch the board to numpy and fix the code to work with it.
* Not doing any other changes yet.
* 1m 17s
* WAAAAAAY slower lol
* Just a bunch of overhead copying between numpy and python. Not using any numpy stuff.
* `_check` goes up to 81% of runtime.

I could try and rewrite check to use matrix templates and stuff but I also sorta wanna try numba out
* Downgraded to 3.10 so I can use numba.

`_check` should be able to just run in native code. It's all loops and math and numpy indexing.

## Use numba on check
* literally just decorate check with @njit()
* down to 9.8 seconds, what is that like 87% faster????
* zero changes to the "manually check every possible victory condition" algorithm.