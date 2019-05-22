#!/usr/bin/env python3
import trigrams,os

global_result = trigrams.read_file("sherlock_small.txt")

def test_read_file():
	assert global_result[0] == "One"
	assert global_result[1] == "night"

def test_build_trigram():
	local_result = trigrams.build_trigram(global_result)
	assert type(local_result) == dict
	assert local_result[('with', 'a')] == ['keen']
	assert local_result[('One', 'night')] == ['it']