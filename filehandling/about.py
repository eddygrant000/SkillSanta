###################################################
    open(file=, mode=)
    open('C:\user\local\Documents\sample.txt') # windows
    open(file='C:\user\local\Documents\sample.txt') # windows
    open('/home/eddy/Documents/data.txt') # linux
    open('data.txt')
---------------------------------------------------
            text file           |           binary file
            notepad:            |   vlc, picaso, xlsx, pdf
                             mode
-----------------------------------------------------------------
        default = t
        default = r
        # advanced = +

        rt : read               |   rb : read
        wt : write              |   wb : write
        at : append             |   ab : append    
-----------------------------------------------------------------

r : 0  # 0123
w : 0
a : end