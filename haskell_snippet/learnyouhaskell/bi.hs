module Main(
Tree,
singleton,
treeInsert,
treeElem,
main,
)
where

data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)

singleton :: a -> Tree a
singleton x = Node x EmptyTree EmptyTree
treeInsert :: (Ord a) => a -> Tree a -> Tree a
treeInsert x EmptyTree = singleton x
treeInsert x (Node a left right)
  | x == a = Node x left right
  | x < a  = Node x (treeInsert x left) right
  | x > a  = Node x left (treeInsert x right)

treeElem :: (Ord a) => a -> Tree a -> Bool
treeElem x EmptyTree = False
treeElem x (Node a left right)
  | x == a = True
  | x < a  = treeElem x left
  | x > a  = treeElem x right


s :: (Num a) => a -> a
s x = x

f a b = foldr treeInsert a b

data TrafficLight = Red | Yellow | Green

instance Eq TrafficLight where
  Red == Red = True
  Green == Green = True
  Yellow == Yellow = True
  _ == _ = False

instance Show TrafficLight where
  show Red = "Red light"
  show Yellow = "Yellow light"
  show Green = "Green light"

class YesNo a where
  yesno :: a -> Bool

instance YesNo Int where
  yesno 0 = False
  yesno _ = True

instance YesNo [a] where
  yesno [] = False
  yesno _ = True

instance YesNo Bool where
  yesno = id

{-
class Functor f where
  fmap :: (a -> b) -> f a -> f b

instance Functor [] where
  fmap = map
-}

class Tofu t where
  tofu :: j a -> t a j

data Frank a b = Frank { frankField :: b a } deriving (Show)

instance Tofu Frank where
  tofu x = Frank x

main = do
  let nums = [8, 6, 4, 1, 7, 3, 5] in
    let numsTree = foldr treeInsert EmptyTree $ nums in
      print $ 1 `treeElem` numsTree

