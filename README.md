# Arithmetic_Coding_for_auxiliary_information_in_DataHiding
Arithmetic Coding for compress the location map or other auxiliary information in steganography or reversible dat hiding.

## Install requirements
`pip install arithmetic-compressor`

## Usage
When we are coding any type of Steganography or Reversible Data Hiding Research, it is important to process the auxiliary information.
In some methods such as Prediction Error Expansion, Histogram Shifting, etc. It yields the location map to record overflow/underflow position information.
In this repository, we provide the code to process the auxiliary inforamtion by arithmetic coding, so that we can compress it and embed it into cover-media.

* Step1: Input your location map by editing the code.
* Step2: Execute the code by: <br>

`python arithmetic_coding.py`

<br>
* In this code, you can check the encoded result, check the size of encoded string, compression rate and you can also decode the encoded string.
Note that the location map usually is presented as symbols "0" and "1".

Good Luck.


