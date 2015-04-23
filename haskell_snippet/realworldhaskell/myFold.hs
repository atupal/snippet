
myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl f z xs = foldr step id xs z
  where step x g a = g (f a x)

main = do
  print $ myFoldl (+) 0 [1,2,3,4,5]
