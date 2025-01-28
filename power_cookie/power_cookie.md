# Power Cookie

## Challenge
Can you get the flag?
Additional details will be available after launching your challenge instance.

## Hints
Do you know how to modify cookies?

## Solution

Given [this](http://saturn.picoctf.net:57013/) site, upon going to the link, an Online Gradebook login appears with a `Continue as guest` option.  
Upon inspecting the cookies as the challenge states, it shows the `isAdmin` value is set to `0`, that is `false`.

![cookie_initial](image.png)

Upon logging in and changing the cookie value to `1` or `true`, the flag is obtained.

![cookie_final](image-1.png)

## Flag
`picoCTF{gr4d3_A_c00k13_5d2505be}`