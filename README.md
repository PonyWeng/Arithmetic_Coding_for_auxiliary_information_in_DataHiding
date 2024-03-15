# Arithmetic_Coding_for_auxiliary_information_in_DataHiding
Arithmetic Coding is used to compress the location map or other auxiliary information in steganography or reversible data hiding.

## Install requirements
`pip install arithmetic-compressor`

## Usage
When coding for any type of Steganography or Reversible Data Hiding research, it is important to process the auxiliary information. In some methods such as Prediction Error Expansion, Histogram Shifting, etc., it yields the location map to record overflow/underflow position data. In this repository, we provide the code to process the auxiliary information using arithmetic coding so that we can compress it and embed it into cover media.

* **Step1:** Input your location map by editing the code.
* **Step2:** Execute the code by: <br>

`python arithmetic_coding.py`

<br>
In this code, you can check the encoded result, examine the size of the encoded string, calculate the compression rate, and decode the encoded string. Please note that the location map is typically represented using symbols "0" and "1".
<br>
<br>
Good Luck.


