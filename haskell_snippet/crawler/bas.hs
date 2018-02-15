import qualified Data.ByteString.Char8 as B
import Data.Tree.NTree.TypeDefs
import Data.Maybe
import Text.XML.HXT.Core
import Control.Monad
import Control.Monad.Trans
import Control.Monad.Maybe
import Network.HTTP
import Network.URI
import System.Environment
import Control.Concurrent.ParallelIO

openUrl :: String ->  MaybeT IO String
openUrl url = case parseURI url of
                Nothing -> fail ""
                Just u -> liftIO (getResponseBody =<< simpleHTTP (mkRequest GET u))

css :: ArrowXml a => String -> a XmlTree XmlTree
css tag = multi (hasName tag)

get :: String -> IO (IOSArrow XmlTree (NTree XNode))
get url = do
  contents <- runMaybeT $ openUrl url
  return $ readString [withParseHTML yes, withWarnings no] (fromMaybe "" contents)

main = do
  url <- parseArgs
  doc <- get url
  imgs <- runX . images $ doc
  -- sequence_ $ map download imgs
  parallel_ $ map download imgs
  stopGlobalPool

convertSlash :: Char -> Char
convertSlash '/' = '-'
convertSlash c = c

images tree = tree >>> css "img" >>> getAttrValue "src"

download url = do
  content <- runMaybeT $ openUrl url
  case content of
    Nothing -> putStrLn $ "bad url: " ++ url
    Just _content -> do
      let name = tail . uriPath . fromJust . parseURI $ url
      let name = map convertSlash name
      print name
      B.writeFile name (B.pack _content)

parseArgs = do
  args <- getArgs
  case args of
    (url:[]) -> return url
    otherwise -> error "usage: getbrabber [url]"
