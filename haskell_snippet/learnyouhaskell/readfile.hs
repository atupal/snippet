import System.IO

main = do
  handle <- openFile "readfile.hs" ReadMode
  contents <- hGetContents handle
  putStr contents
  hClose handle
