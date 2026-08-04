### General registers
Number series in General registers for server printers and Agent tasks.
Package number
- SSCC package numbers normally used for package identification should also be registered here.
- OSCAR (Odette) Package numbers (OD) – A number series for package numbers that has been created by and is administered by Odette.
- DUNS Package number (UN) – A number series that has been created and is administered by Dun & Bradstreet.
- JIPDEC Package number (LA) – A number series that is administered by Japan Institute for Promotion of Digital Economy and Community (JIPDEC).

#### Number series
The name of the number series.

#### Initial number
SSCC package number. Here you can enter an initial number for this number series.

#### Prefix
SSCC package number. Here you can enter a prefix for the number series. Prefixes are obtained from GS1.
OSCAR (Odette) Package number (OD). Here you enter the given company prefix. This can contain a maximum of 6 characters. Do not include the issued code OD here, this is added automatically.
DUNS Package number (UN). Here you enter the given company prefix. This can contain a maximum of 9 characters. Do not include the issued code UN here, this is added automatically.
JIPDEC Package number (LA). Here you enter the given company prefix. This can contain a maximum of 13 characters. Do not include the issued code LA here, this is added automatically.

#### Next number
Here you can see the next number that will be used in the number series.

#### Greatest number used
Here you can see the greatest number that has been used in the number series. It is useful to see if there is a need to adjust the number series in order for it not to clash with previously used numbers.

#### Start number
All package number series. Start number for this number series. For SSCC package numbers you retrieve the start number from GS1.

#### End number.
All package number series. End number for this number series. For SSCC package numbers you retrieve the end number from GS1.

#### Warn when remainder is:
All package number series. Here you enter when Monitor ERP should warn that the number series is approaching the final number in the interval.

#### Increment initial number automatically
SSCC package number. Here you decide if the initial number should be incremented automatically and start over from the Start number when the top limit has been reached. This can be done as long as the initial number is less than 9.

#### U (Use notifications)
Here you decide if notifications should be used to let users, groups or roles know that the SSCC number series is about to end or has ended.

#### N (Notifications)
Here you decide which users, groups or roles that should receive a notification in the message center letting them know the number series is about to end or has ended.
How is an SSCC package number created?
The SSCC number consists of multiple logical parts and there is a number of columns used to configure this:
NFFFFFFFFFAAAAAAAK
- N – An initial number between 0 and 9. This is entered in the Initial number column.
- F – GS1 company prefix. This is entered in the Prefix column.
- A – Serial number A serial number is a number that is used for traceability for parts on entity level., right aligned, and completed with 0 (zeros) to fill the positions not used. You enter the start number in the Start number column (without leading zeros).
- K – A check digit.
