import ctypes

function = ctypes.CDLL('./main.dll') 
function.main()