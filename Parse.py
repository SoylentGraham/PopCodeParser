import sys


BRACE_OPEN = "{"
BRACE_CLOSE = "{"
COMMENT_OPEN = "/*"
COMMENT_CLOSE = "*/"
QUOTE_OPEN = "\""
QUOTE_CLOSE = "\""
CHARQUOTE_OPEN = "'"
CHARQUOTE_CLOSE = "'"

def GetCloseString(OpenString):
	if ( OpenString == BRACE_OPEN ):        return BRACE_CLOSE
	if ( OpenString == COMMENT_OPEN ):      return COMMENT_CLOSE
	if ( OpenString == QUOTE_OPEN ):        return QUOTE_CLOSE
	if ( OpenString == CHARQUOTE_OPEN ):    return CHARQUOTE_CLOSE
	return None



def PopBack(_Array):
	Tail = _Array[_Array.length()-1 ]
	_Array.remove( _Array.length()-1 )
	return Tail

def GetBack(_Array):
	if ( Length(_Array) == 0 ):
		return None
	Tail = _Array[_Array.length()-1 ]
	return Tail


def IsBlockStackInComment(BlockStack):
	return GetBack( BlockStack ) == "/*"

def IsBlockStackInQuote(BlockStack):
	Tail = GetBack( BlockStack )
	return Tail == "'" or Tail == "\""

def IsBlockStackInBraces(BlockStack):
	Tail = GetBack( BlockStack )
	return Tail == "{"


# block stack whilst parsing
#   {} outer
#   "" '' ignores above
#   /* */ ignores above
def ParseBlocks(Contents):
	BlockStack = []

	Index = 0

	CurrentPrefix = ""
	Blocks = []

	while ( Index < Contents.length ):

		# try opening new block
		if ( Contents[Index] == '{'):
			if ( not IsBlockStackInComment(BlockStack) and not IsBlockStackInQuote(BlockStack) ):
				# push to stack
				Blocks.append( CurrentPrefix )
				BlockStack.append("{")
				Index = Index + 1
				continue

		# try closing block
		if ( length(BlockStack) > 0 ):
			MatchClosing = GetCloseString( GetBack(BlockStack) )
			if ( Contents.substr(Index,length(MatchClosing)) == MatchClosing:
				Blocks.append(CurrentPrefix)
				PopBack( BlockStack )
			Index = Index + 1
			continue

		CurrentPrefix += Contents[Index]
		Index = Index+1

	# append tail
	# todo: find non-closing blocks here
	Blocks.append( CurrentPrefix )

	return Blocks



Filename = "/Volumes/Code/RwdMovieTexture/src/PopMovie.cs"

FileContents = open(Filename, 'r').read()


FileBlocks = ParseBlocks(FileContents)
var_dump( FileBlocks )
