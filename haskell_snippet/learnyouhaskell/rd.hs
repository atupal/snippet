

data Section = Section {
  getA :: Int,
  getB :: Int,
  getC :: Int
  } deriving (Show)

type RoadSystem = [Section]

data Label = A | B | C deriving (Show)
type Path = [(Label, Int)]

roadStep :: (Path, Path) -> Section -> (Path, Path)
roadStep (pathA, pathB) (Section a b c) =
  let timeA = sum (map snd pathA)
      timeB = sum (map snd pathB)
      forwardTimeToA = timeA + a
      crossTimeToA = timeB + b + c
      forwardTimeToB = timeB + b
      crossTimeToB = timeA + a + c
      newPathToA = if forwardTimeToA <= crossTimeToA
                      then (A, a):pathA
                      else (C, c):(B, b):pathB
      newPathToB = if forwardTimeToB <= crossTimeToB
                      then (B, b):pathB
                      else (C, c):(A, a):pathA
  in (newPathToA, newPathToB)


main :: IO ()
main = do
  return ()
