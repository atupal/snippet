import System.Environment
import System.IO
import System.Directory
import Data.List

dispatch :: [ ( String, [String] -> IO ()) ]
dispatch = [("add", add),
            ("view", view),
            ("remove", remove)
            ]

add :: [String] -> IO ()
add [fileName, todoItem] = appendFile fileName (todoItem ++ "\n")

view :: [String] -> IO ()
view [fileName] = do
  contents <- readFile fileName
  let todoTasks = lines contents
      numberedTasks = zipWith(\ n line -> show n ++ " - " ++ line) [0..] todoTasks
  putStr $ unlines numberedTasks

remove :: [String] -> IO ()
remove [fileName, numberString] = do
  handle <- openFile fileName ReadMode
  tempdir <- getTemporaryDirectory
  (tempName, tempHandle) <- openTempFile tempdir "temp"
  contents <- hGetContents handle
  let number = read numberString
      todoTasks = lines contents
      newTodoItems = delete (todoTasks !! number) todoTasks
  hPutStr tempHandle $ unlines newTodoItems
  hClose handle
  hClose tempHandle
  removeFile fileName
  renameFile tempName fileName

main = do
  (command:args) <- getArgs
  let (Just action) = lookup command dispatch
  action args
