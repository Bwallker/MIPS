default:
    @just --list

release +args="":
    @just build {{args}} -O3

build +args="":
    mips-img-elf-gcc -march=mips2 {{args}} -S -s -g0 ./c-src/*.c -o main.asm

help:
    mips-img-elf-gcc --help

compiler +args="":
    mips-img-elf-gcc {{args}}