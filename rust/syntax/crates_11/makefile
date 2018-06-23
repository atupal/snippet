.DEFAULT_GOAL := executable

library.rlib: rary.rs
	rustc --crate-type=lib rary.rs

executable: executable.rs library.rlib
	rustc executable.rs --extern rary=library.rlib
