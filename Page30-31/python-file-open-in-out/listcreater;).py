import random

"""This takes a list of names from the internet, and pairs their first name with a random(ish) integer.
And then prints the output"""

names = """Kristina 	Chung 	H 	Kristina H. Chung 	Chung, Kristina H.
Paige 	Chen 	H 	Paige H. Chen 	Chen, Paige H.
Sherri 	Melton 	E 	Sherri E. Melton 	Melton, Sherri E.
Gretchen 	Hill 	I 	Gretchen I. Hill 	Hill, Gretchen I.
Karen 	Puckett 	U 	Karen U. Puckett 	Puckett, Karen U.
Patrick 	Song 	O 	Patrick O. Song 	Song, Patrick O.
Elsie 	Hamilton 	A 	Elsie A. Hamilton 	Hamilton, Elsie A.
Hazel 	Bender 	E 	Hazel E. Bender 	Bender, Hazel E.
Malcolm 	Wagner 	A 	Malcolm A. Wagner 	Wagner, Malcolm A.
Dolores 	McLaughlin 	C 	Dolores C. McLaughlin 	McLaughlin, Dolores C.
Francis 	McNamara 	C 	Francis C. McNamara 	McNamara, Francis C.
Sandy 	Raynor 	A 	Sandy A. Raynor 	Raynor, Sandy A.
Marion 	Moon 	O 	Marion O. Moon 	Moon, Marion O.
Beth 	Woodard 	O 	Beth O. Woodard 	Woodard, Beth O.
Julia 	Desai 	E 	Julia E. Desai 	Desai, Julia E.
Jerome 	Wallace 	A 	Jerome A. Wallace 	Wallace, Jerome A.
Neal 	Lawrence 	A 	Neal A. Lawrence 	Lawrence, Neal A.
Jean 	Griffin 	R 	Jean R. Griffin 	Griffin, Jean R.
Kristine 	Dougherty 	O 	Kristine O. Dougherty 	Dougherty, Kristine O.
Crystal 	Powers 	O 	Crystal O. Powers 	Powers, Crystal O.
Alex 	May 	A 	Alex A. May 	May, Alex A.
Eric 	Steele 	T 	Eric T. Steele 	Steele, Eric T.
Wesley 	Teague 	E 	Wesley E. Teague 	Teague, Wesley E.
Franklin 	Vick 	I 	Franklin I. Vick 	Vick, Franklin I.
Claire 	Gallagher 	A 	Claire A. Gallagher 	Gallagher, Claire A.
Marian 	Solomon 	O 	Marian O. Solomon 	Solomon, Marian O.
Marcia 	Walsh 	A 	Marcia A. Walsh 	Walsh, Marcia A.
Dwight 	Monroe 	O 	Dwight O. Monroe 	Monroe, Dwight O.
Wayne 	Connolly 	O 	Wayne O. Connolly 	Connolly, Wayne O.
Stephanie 	Hawkins 	A 	Stephanie A. Hawkins 	Hawkins, Stephanie A.
Neal 	Middleton 	I 	Neal I. Middleton 	Middleton, Neal I.
Gretchen 	Goldstein 	O 	Gretchen O. Goldstein 	Goldstein, Gretchen O.
Tim 	Watts 	A 	Tim A. Watts 	Watts, Tim A.
Jerome 	Johnston 	O 	Jerome O. Johnston 	Johnston, Jerome O.
Shelley 	Weeks 	E 	Shelley E. Weeks 	Weeks, Shelley E.
Priscilla 	Wilkerson 	I 	Priscilla I. Wilkerson 	Wilkerson, Priscilla I.
Elsie 	Barton 	A 	Elsie A. Barton 	Barton, Elsie A.
Beth 	Walton 	A 	Beth A. Walton 	Walton, Beth A.
Erica 	Hall 	A 	Erica A. Hall 	Hall, Erica A.
Douglas 	Ross 	O 	Douglas O. Ross 	Ross, Douglas O.
Donald 	Chung 	H 	Donald H. Chung 	Chung, Donald H.
Katherine 	Bender 	E 	Katherine E. Bender 	Bender, Katherine E.
Paul 	Woods 	O 	Paul O. Woods 	Woods, Paul O.
Patricia 	Mangum 	A 	Patricia A. Mangum 	Mangum, Patricia A.
Lois 	Joseph 	O 	Lois O. Joseph 	Joseph, Lois O.
Louis 	Rosenthal 	O 	Louis O. Rosenthal 	Rosenthal, Louis O.
Christina 	Bowden 	O 	Christina O. Bowden 	Bowden, Christina O.
Darlene 	Barton 	A 	Darlene A. Barton 	Barton, Darlene A.
Harvey 	Underwood 	N 	Harvey N. Underwood 	Underwood, Harvey N.
William 	Jones 	O 	William O. Jones 	Jones, William O.
Frederick 	Baker 	A 	Frederick A. Baker 	Baker, Frederick A.
Shirley 	Merritt 	E 	Shirley E. Merritt 	Merritt, Shirley E.
Jason 	Cross 	R 	Jason R. Cross 	Cross, Jason R.
Judith 	Cooper 	O 	Judith O. Cooper 	Cooper, Judith O.
Gretchen 	Holmes 	O 	Gretchen O. Holmes 	Holmes, Gretchen O.
Don 	Sharpe 	H 	Don H. Sharpe 	Sharpe, Don H.
Glenda 	Morgan 	O 	Glenda O. Morgan 	Morgan, Glenda O.
Scott 	Hoyle 	O 	Scott O. Hoyle 	Hoyle, Scott O.
Pat 	Allen 	L 	Pat L. Allen 	Allen, Pat L.
Michelle 	Rich 	I 	Michelle I. Rich 	Rich, Michelle I.
Jessica 	Rich 	I 	Jessica I. Rich 	Rich, Jessica I.
Evan 	Grant 	R 	Evan R. Grant 	Grant, Evan R.
Melinda 	Proctor 	R 	Melinda R. Proctor 	Proctor, Melinda R.
Calvin 	Diaz 	I 	Calvin I. Diaz 	Diaz, Calvin I.
Eugene 	Graham 	R 	Eugene R. Graham 	Graham, Eugene R.
Vickie 	Watkins 	A 	Vickie A. Watkins 	Watkins, Vickie A.
Luis 	Hinton 	I 	Luis I. Hinton 	Hinton, Luis I.
Allan 	Marsh 	A 	Allan A. Marsh 	Marsh, Allan A.
Melanie 	Hewitt 	E 	Melanie E. Hewitt 	Hewitt, Melanie E.
Marianne 	Branch 	R 	Marianne R. Branch 	Branch, Marianne R.
Natalie 	Walton 	A 	Natalie A. Walton 	Walton, Natalie A.
Caroline 	O'Brien 	' 	Caroline '. O'Brien 	O'Brien, Caroline '.
Arlene 	Case 	A 	Arlene A. Case 	Case, Arlene A.
Kyle 	Watts 	A 	Kyle A. Watts 	Watts, Kyle A.
Calvin 	Christensen 	H 	Calvin H. Christensen 	Christensen, Calvin H.
Gary 	Parks 	A 	Gary A. Parks 	Parks, Gary A.
Samantha 	Hardin 	A 	Samantha A. Hardin 	Hardin, Samantha A.
Sara 	Lucas 	U 	Sara U. Lucas 	Lucas, Sara U.
Stacy 	Eason 	A 	Stacy A. Eason 	Eason, Stacy A.
Gladys 	Davidson 	A 	Gladys A. Davidson 	Davidson, Gladys A.
Mike 	Whitehead 	H 	Mike H. Whitehead 	Whitehead, Mike H.
Lynne 	Rose 	O 	Lynne O. Rose 	Rose, Lynne O.
Faye 	Sparks 	P 	Faye P. Sparks 	Sparks, Faye P.
Diana 	Moore 	O 	Diana O. Moore 	Moore, Diana O.
Leon 	Pearson 	E 	Leon E. Pearson 	Pearson, Leon E.
Ethel 	Rodgers 	O 	Ethel O. Rodgers 	Rodgers, Ethel O.
Steve 	Graves 	R 	Steve R. Graves 	Graves, Steve R.
Alison 	Scarborough 	C 	Alison C. Scarborough 	Scarborough, Alison C.
Sherri 	Sutton 	U 	Sherri U. Sutton 	Sutton, Sherri U.
Patsy 	Sinclair 	I 	Patsy I. Sinclair 	Sinclair, Patsy I.
Kelly 	Bowman 	O 	Kelly O. Bowman 	Bowman, Kelly O.
Stacy 	Olsen 	L 	Stacy L. Olsen 	Olsen, Stacy L.
Curtis 	Love 	O 	Curtis O. Love 	Love, Curtis O.
Dana 	McLean 	C 	Dana C. McLean 	McLean, Dana C.
Jennifer 	Christian 	H 	Jennifer H. Christian 	Christian, Jennifer H.
Brett 	Lamb 	A 	Brett A. Lamb 	Lamb, Brett A.
Brandon 	James 	A 	Brandon A. James 	James, Brandon A.
Keith 	Chandler 	H 	Keith H. Chandler 	Chandler, Keith H.
Joann 	Stout 	T 	Joann T. Stout 	Stout, Joann T."""

names = names.split('\n')
firsts = []
for name in names:
    first = name.split(' 	')[0]
    firsts.append(first)
for first in firsts:
    print first+':'+`random.randint(1,100)`
