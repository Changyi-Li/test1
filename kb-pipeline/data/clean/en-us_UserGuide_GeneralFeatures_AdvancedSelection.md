### Advanced selection
It is possible to perform a more specified selection in list procedures by using wildcard characters in the From field under the Selection tab in the procedures. When you use wildcards, the To field becomes inactive. Only when using the wildcard " !", the To field is available to use. The supported wildcards and expressions and how to use them are described in the table below.
| Expression | Explanation | Examples |
|---|---|---|
| % | The percentage sign "%" selects everything before or after the sign. | pl% – will include everything starting with "pl". %rg – will include everything ending with "rg". %ul% – will include everything containing "ul". |
| ! | Exclamation mark with an or several initial spaces " !" can be used to select by a single number. You enter multiple spaces in case there are spaces in the part number and you are unsure of how many that are used. | 5000 in the From field and 5000 ! in the To field – will only include the specific number "5000". |
| _ | Underscore "_" selects everything in the indicated position, including space. | _ _ _ _lock – will include everything which contains 8 character and ends with "lock". |
| [n-n] | Square brackets "[ ]" containing the expressions "n-n", "nn", or "^n" must always be combined with the wildcards Percent "%" or Underscore "_" and can be used to select both numbers and text. | 5[3-5]9% – will include everything starting with 539, 549, and 559. _[2-6]% – will include everything with 2, 3, 4, 5, and 6 in the second position. |
| [nn] |   | %[25] – will include everything ending with either 2 or 5. |
| [^n] | Circumflex "^" is used to exclude the character to the right of the symbol. | 7[^4]% – will include everything beginning with 7 and which does not have 4 in the second position. |
| [^n^n] |   | 5[^2^4]% – will include everything starting with 5 and which does not have 2 or 4 in the second position. |
