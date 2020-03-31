# Reads the first and original Octal Numbers I imported into a text file
# f = open("ascii.txt", "r")
# lines = f.read().replace(',', ' ')

# #Wrote a function that after reading the text file it will convert the integers into characters
# def octal_to_str(octal_str):

#     message = ""
#     for octal_char in octal_str.split(" "):
#         message += chr(int(octal_char, 8))
#     return message

# print(octal_to_str(lines))


# FIRST SOLUTION
# You made it to Level 1. Your level password is: AE2C45DC5F9EE6C0. The next message is: 596f75206d61646520697420746f204c6576656c20322e20596f7572206c6576656c2070617373776f72642069733a20343645423734443036384330353438362e20546865206e657874206d6573736167652069733a2057573931494731685a4755676158516764473867624756325a5777674d79456753473976636d466f495341365243425561475567624756325a5777676347467a63336476636d516761584d36494441774e6a4d314e6a593351305177526b564452454d754946567a5a534270644342306279426b5a574e765a4755676447686c4947356c654851676257567a6332466e5a53416f53456c4f56446f675347563449476c7a4948526f5a5342305a5868304c694244636d397a63794230614755675431496764326c3061434230614755676347467a637934704f6941324f54566d4e444d784d7a55344e5463314d6a55794e6a4d795a4451304e6a63324e5446684d6d497a4e6a51794d544131595455324e444d314d7a56684d54637a4d7a49314e444d7a4e544d794d6d4d7a4e6a49334d5441314f5451314d446b784e5463334d4759334e6a41794e7a49334e6a63784e7a4d334e4463334d4449334e6a41314d444977595463304d5467784e6a63784d6d4d7a4e6a45774d6a4d7a5a444d334d7a59794d6a45774e544d304e4455324e5445315a6a51794d5749324d7a49774e5455794e544a684d6a63794d54597a4e4451314f44557a4d544d314d7a566d4e5467314e6a4a6d4e6a51304d4449334d7a597a4d444d7a4d6d4d304d6a55304d545978596a646b4e3259334f44597a4e7a6b324e4441784e7a55324e544a684d7a63324d7a51304e5467314d7a457a4e5749304d7a56694e5455794e6a4d324d546b33597a59314d544d774e6a41314d4755775a4463774d4751324e54637a4e7a67334e54426a4e7a6b324d6a41324e32453d

# ## I then imported the next encrypted message in another text file to read
# hex = open("ascii2.txt", "r")
# h_lines = hex.read().replace(' ', ',')
# n = 2
# hex_lines = [h_lines[i:i+n] for i in range(0, len(h_lines), 2)]
# print(' '.join(hex_lines))


# hex2 = open("ascii3.txt", "r")
# h2lines = hex2.read().replace(' ', ',')
# n = 2
# hex2_lines = [h2lines[i:i+n] for i in range(0, len(h2lines), 2)]
# print(' '.join(hex2_lines))

# # Wrote a new function that then converts the Hex numbers to text 
# def hex_to_str(hex_str):

#     message = " "
#     for hex_char in hex_str:
#         message += chr(int(hex_char.encode(),16))
#         print(message)
#     return message

# print(hex_to_str(hex_lines))

## SECOND SOLUTION
#  You made it to Level 2. Your level password is: 46EB74D068C05486. The next message is: WW91IG1hZGUgaXQgdG8gbGV2ZWwgMyEgSG9vcmFoISA6RCBUaGUgbGV2ZWwgcGFzc3dvcmQgaXM6IDAwNjM1NjY3Q0QwRkVDREMuIFVzZSBpdCB0byBkZWNvZGUgdGhlIG5leHQgbWVzc2FnZSAoSElOVDogSGV4IGlzIHRoZSB0ZXh0LiBDcm9zcyB0aGUgT1Igd2l0aCB0aGUgcGFzcy4pOiA2OTVmNDMxMzU4NTc1MjUyNjMyZDQ0Njc2NTFhMmIzNjQyMTA1YTU2NDM1MzVhMTczMzI1NDMzNTMyMmMzNjI3MTA1OTQ1MDkxNTc3MGY3NjAyNzI3NjcxNzM3NDc3MDI3NjA1MDIwYTc0MTgxNjcxMmMzNjEwMjMzZDM3MzYyMjEwNTM0NDU2NTE1ZjQyMWI2MzIwNTUyNTJhMjcyMTYzNDQ1ODUzMTM1MzVmNTg1NjJmNjQ0MDI3MzYzMDMzMmM0MjU0MTYxYjdkN2Y3ODYzNzk2NDAxNzU2NTJhMzc2MzQ0NTg1MzEzNWI0MzViNTUyNjM2MTk3YzY1MTMwNjA1MGUwZDcwMGQ2NTczNzg3NTBjNzk2MjA2N2E=

# I then decoded the next level using the base64 decoder through Python
##Decoding base64
import base64
coded_string='WW91IG1hZGUgaXQgdG8gbGV2ZWwgMyEgSG9vcmFoISA6RCBUaGUgbGV2ZWwgcGFzc3dvcmQgaXM6IDAwNjM1NjY3Q0QwRkVDREMuIFVzZSBpdCB0byBkZWNvZGUgdGhlIG5leHQgbWVzc2FnZSAoSElOVDogSGV4IGlzIHRoZSB0ZXh0LiBDcm9zcyB0aGUgT1Igd2l0aCB0aGUgcGFzcy4pOiA2OTVmNDMxMzU4NTc1MjUyNjMyZDQ0Njc2NTFhMmIzNjQyMTA1YTU2NDM1MzVhMTczMzI1NDMzNTMyMmMzNjI3MTA1OTQ1MDkxNTc3MGY3NjAyNzI3NjcxNzM3NDc3MDI3NjA1MDIwYTc0MTgxNjcxMmMzNjEwMjMzZDM3MzYyMjEwNTM0NDU2NTE1ZjQyMWI2MzIwNTUyNTJhMjcyMTYzNDQ1ODUzMTM1MzVmNTg1NjJmNjQ0MDI3MzYzMDMzMmM0MjU0MTYxYjdkN2Y3ODYzNzk2NDAxNzU2NTJhMzc2MzQ0NTg1MzEzNWI0MzViNTUyNjM2MTk3YzY1MTMwNjA1MGUwZDcwMGQ2NTczNzg3NTBjNzk2MjA2N2E='

code_message = base64.b64decode(coded_string)

print(code_message)

# THIRD LEVEL RESULT FROM Decoder
# 'You made it to level 3! Hoorah! :D The level password is: 00635667CD0FECDC. Use it to decode the next message (HINT: Hex is the text. Cross the OR with the pass.): 695f431358575252632d4467651a2b3642105a5643535a1733254335322c36271059450915770f7602727671737477027605020a741816712c3610233d37362210534456515f421b632055252a27216344585313535f58562f6440273630332c4254161b7d7f786379640175652a3763445853135b435b552636197c651306050e0d700d657378750c7962067a'

# The next level was definitely challenging but after doing some research and reading through the hint 50 or so times. I was able to figure out that I needed to decode the message using XOR (which I used an online XOR converter with the password from level 3) which then gave me the result of :

# FOURTH LEVEL RESUlT
# You made it! Your level password is: A9AA6F7673AF549A. For extra credit, decode the final password (HINT: 13 is the number): PBF>=F>PENBO=R@?

# The last result I saw the answer was in base64 and was able to work out using ROT13. Which I could assume would be in reverse so subtracting each character by 13 places giving me :

# C591091C8A5B0E32

# I have included each levels password and the last answer since it the same length as the passwords.
## Each Level Password
# AE2C45DC5F9EE6C0
# 46EB74D068C05486
# 00635667CD0FECDC
# A9AA6F7673AF549A
# Final Solution
# C591091C8A5B0E32



# 'You made it to level 3! Hoorah! :D The level password is: 00635667CD0FECDC. Use it to decode the next message (HINT: Hex is the text. Cross the OR with the pass.): 695f431358575252632d4467651a2b3642105a5643535a1733254335322c36271059450915770f7602727671737477027605020a741816712c3610233d37362210534456515f421b632055252a27216344585313535f58562f6440273630332c4254161b7d7f786379640175652a3763445853135b435b552636197c651306050e0d700d657378750c7962067a'



# coded_string='AE2C45DC5F9EE6C0 46EB74D068C05486 00635667CD0FECDC A9AA6F7673AF549A C591091C8A5B0E32'