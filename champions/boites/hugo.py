def ia(boxes):
    n=len(boxes)
    rep="D"
    if n>1:
        g=(boxes[0]-boxes[1])+(boxes[0]-boxes[n-1])
        d=(boxes[n-1]-boxes[n-2])+(boxes[n-1]-boxes[0])
        if g>d:
            rep="G"
    return rep