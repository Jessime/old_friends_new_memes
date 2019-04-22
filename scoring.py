TABLE_STYLE_THINBORDER = "border: 1px solid #000000; border-collapse: collapse;"
#TABLE_STYLE_THINBORDER = "border: 1px solid #000000;"

class TableCell (object):
    """
    a TableCell object is used to create a cell in a HTML table. (TD or TH)
    Attributes:
    - text: text in the cell (may contain HTML tags). May be any object which
            can be converted to a string using str().
    - header: bool, false for a normal data cell (TD), true for a header cell (TH)
    - bgcolor: str, background color
    - width: str, width
    - align: str, horizontal alignement (left, center, right, justify or char)
    - char: str, alignment character, decimal point if not specified
    - charoff: str, see HTML specs
    - valign: str, vertical alignment (top|middle|bottom|baseline)
    - style: str, CSS style
    - attribs: dict, additional attributes for the TD/TH tag
    Reference: http://www.w3.org/TR/html4/struct/tables.html#h-11.2.6
    """

    def __init__(self, text="", bgcolor=None, header=False, width=None,
                align=None, char=None, charoff=None, valign=None, style=None,
                attribs=None):
        """TableCell constructor"""
        self.text    = text
        self.bgcolor = bgcolor
        self.header  = header
        self.width   = width
        self.align   = align
        self.char    = char
        self.charoff = charoff
        self.valign  = valign
        self.style   = style
        self.attribs = attribs
        if attribs==None:
            self.attribs = {}

    def __str__(self):
        """return the HTML code for the table cell as a string"""
        attribs_str = ""
        if self.bgcolor: self.attribs['bgcolor'] = self.bgcolor
        if self.width:   self.attribs['width']   = self.width
        if self.align:   self.attribs['align']   = self.align
        if self.char:    self.attribs['char']    = self.char
        if self.charoff: self.attribs['charoff'] = self.charoff
        if self.valign:  self.attribs['valign']  = self.valign
        if self.style:   self.attribs['style']   = self.style
        for attr in self.attribs:
            attribs_str += ' %s="%s"' % (attr, self.attribs[attr])
        if self.text is not None:
            text = str(self.text)
        else:
            # An empty cell should at least contain a non-breaking space
            text = '&nbsp;'
        if self.header:
            return '  <TH%s>%s</TH>\n' % (attribs_str, text)
        else:
            return '  <TD%s>%s</TD>\n' % (attribs_str, text)

#-------------------------------------------------------------------------------

class TableRow (object):
    """
    a TableRow object is used to create a row in a HTML table. (TR tag)
    Attributes:
    - cells: list, tuple or any iterable, containing one string or TableCell
             object for each cell
    - header: bool, true for a header row (TH), false for a normal data row (TD)
    - bgcolor: str, background color
    - col_align, col_valign, col_char, col_charoff, col_styles: see Table class
    - attribs: dict, additional attributes for the TR tag
    Reference: http://www.w3.org/TR/html4/struct/tables.html#h-11.2.5
    """

    def __init__(self, cells=None, bgcolor=None, header=False, attribs=None,
                col_align=None, col_valign=None, col_char=None,
                col_charoff=None, col_styles=None):
        """TableCell constructor"""
        self.bgcolor     = bgcolor
        self.cells       = cells
        self.header      = header
        self.col_align   = col_align
        self.col_valign  = col_valign
        self.col_char    = col_char
        self.col_charoff = col_charoff
        self.col_styles  = col_styles
        self.attribs     = attribs
        if attribs==None:
            self.attribs = {}

    def __str__(self):
        """return the HTML code for the table row as a string"""
        attribs_str = ""
        if self.bgcolor: self.attribs['bgcolor'] = self.bgcolor
        for attr in self.attribs:
            attribs_str += ' %s="%s"' % (attr, self.attribs[attr])
        result = ' <TR%s>\n' % attribs_str
        for cell in self.cells:
            col = self.cells.index(cell)    # cell column index
            if not isinstance(cell, TableCell):
                cell = TableCell(cell, header=self.header)
            # apply column alignment if specified:
            if self.col_align and cell.align==None:
                cell.align = self.col_align[col]
            if self.col_char and cell.char==None:
                cell.char = self.col_char[col]
            if self.col_charoff and cell.charoff==None:
                cell.charoff = self.col_charoff[col]
            if self.col_valign and cell.valign==None:
                cell.valign = self.col_valign[col]
            # apply column style if specified:
            if self.col_styles and cell.style==None:
                cell.style = self.col_styles[col]
            result += str(cell)
        result += ' </TR>\n'
        return result

#-------------------------------------------------------------------------------

class Table (object):
    """
    a Table object is used to create a HTML table. (TABLE tag)
    Attributes:
    - rows: list, tuple or any iterable, containing one iterable or TableRow
            object for each row
    - header_row: list, tuple or any iterable, containing the header row (optional)
    - border: str or int, border width
    - style: str, table style in CSS syntax (thin black borders by default)
    - width: str, width of the table on the page
    - attribs: dict, additional attributes for the TABLE tag
    - col_width: list or tuple defining width for each column
    - col_align: list or tuple defining horizontal alignment for each column
    - col_char: list or tuple defining alignment character for each column
    - col_charoff: list or tuple defining charoff attribute for each column
    - col_valign: list or tuple defining vertical alignment for each column
    - col_styles: list or tuple of HTML styles for each column
    Reference: http://www.w3.org/TR/html4/struct/tables.html#h-11.2.1
    """

    def __init__(self, rows=None, border='1', style=None, width=None,
                cellspacing=None, cellpadding=4, attribs=None, header_row=None,
                col_width=None, col_align=None, col_valign=None,
                col_char=None, col_charoff=None, col_styles=None):
        """TableCell constructor"""
        self.border = border
        self.style = style
        # style for thin borders by default
        if style == None: self.style = TABLE_STYLE_THINBORDER
        self.width       = width
        self.cellspacing = cellspacing
        self.cellpadding = cellpadding
        self.header_row  = header_row
        self.rows        = rows
        if not rows: self.rows = []
        self.attribs     = attribs
        if not attribs: self.attribs = {}
        self.col_width   = col_width
        self.col_align   = col_align
        self.col_char    = col_char
        self.col_charoff = col_charoff
        self.col_valign  = col_valign
        self.col_styles  = col_styles

    def __str__(self):
        """return the HTML code for the table as a string"""
        attribs_str = ""
        if self.border: self.attribs['border'] = self.border
        if self.style:  self.attribs['style'] = self.style
        if self.width:  self.attribs['width'] = self.width
        if self.cellspacing:  self.attribs['cellspacing'] = self.cellspacing
        if self.cellpadding:  self.attribs['cellpadding'] = self.cellpadding
        for attr in self.attribs:
            attribs_str += ' %s="%s"' % (attr, self.attribs[attr])
        result = '<TABLE%s>\n' % attribs_str
        # insert column tags and attributes if specified:
        if self.col_width:
            for width in self.col_width:
                result += '  <COL width="%s">\n' % width
        # The following code would also generate column attributes for style
        # and alignement according to HTML4 specs,
        # BUT it is not supported completely (only width) on Mozilla Firefox:
        # see https://bugzilla.mozilla.org/show_bug.cgi?id=915
##        n_cols = max(len(self.col_styles), len(self.col_width),
##                     len(self.col_align), len(self.col_valign))
##        for i in range(n_cols):
##            col = ''
##            try:
##                if self.col_styles[i]:
##                    col += ' style="%s"' % self.col_styles[i]
##            except: pass
##            try:
##                if self.col_width[i]:
##                    col += ' width="%s"' % self.col_width[i]
##            except: pass
##            try:
##                if self.col_align[i]:
##                    col += ' align="%s"' % self.col_align[i]
##            except: pass
##            try:
##                if self.col_valign[i]:
##                    col += ' valign="%s"' % self.col_valign[i]
##            except: pass
##            result += '<COL%s>\n' % col
        # First insert a header row if specified:
        if self.header_row:
            if not isinstance(self.header_row, TableRow):
                result += str(TableRow(self.header_row, header=True))
            else:
                result += str(self.header_row)
        # Then all data rows:
        for row in self.rows:
            if not isinstance(row, TableRow):
                row = TableRow(row)
            # apply column alignments  and styles to each row if specified:
            # (Mozilla bug workaround)
            if self.col_align and not row.col_align:
                row.col_align = self.col_align
            if self.col_char and not row.col_char:
                row.col_char = self.col_char
            if self.col_charoff and not row.col_charoff:
                row.col_charoff = self.col_charoff
            if self.col_valign and not row.col_valign:
                row.col_valign = self.col_valign
            if self.col_styles and not row.col_styles:
                row.col_styles = self.col_styles
            result += str(row)
        result += '</TABLE>'
        return result


#-------------------------------------------------------------------------------

class List (object):
    """
    a List object is used to create an ordered or unordered list in HTML.
    (UL/OL tag)
    Attributes:
    - lines: list, tuple or any iterable, containing one string for each line
    - ordered: bool, choice between an ordered (OL) or unordered list (UL)
    - attribs: dict, additional attributes for the OL/UL tag
    Reference: http://www.w3.org/TR/html4/struct/lists.html
    """

    def __init__(self, lines=None, ordered=False, start=None, attribs=None):
        """List constructor"""
        if lines:
            self.lines = lines
        else:
            self.lines = []
        self.ordered = ordered
        self.start = start
        if attribs:
            self.attribs = attribs
        else:
            self.attribs = {}

    def __str__(self):
        """return the HTML code for the list as a string"""
        attribs_str = ""
        if self.start:  self.attribs['start'] = self.start
        for attr in self.attribs:
            attribs_str += ' %s="%s"' % (attr, self.attribs[attr])
        if self.ordered: tag = 'OL'
        else:            tag = 'UL'
        result = '<%s%s>\n' % (tag, attribs_str)
        for line in self.lines:
            result += ' <LI>%s\n' % str(line)
        result += '</%s>\n' % tag
        return result


##class Link (object):
##    """
##    a Link object is used to create link in HTML. (<a> tag)
##
##    Attributes:
##    - text: str, text of the link
##    - url: str, URL of the link
##    - attribs: dict, additional attributes for the A tag
##
##    Reference: http://www.w3.org/TR/html4
##    """
##
##    def __init__(self, text, url=None, attribs=None):
##        """Link constructor"""
##        self.text = text
##        self.url = url
##        if attribs:
##            self.attribs = attribs
##        else:
##            self.attribs = {}
##
##    def __str__(self):
##        """return the HTML code for the link as a string"""
##        attribs_str = ""
##        if self.url:  self.attribs['href'] = self.url
##        for attr in self.attribs:
##            attribs_str += ' %s="%s"' % (attr, self.attribs[attr])
##        return '<a%s>%s</a>' % (attribs_str, text)


#=== FUNCTIONS ================================================================

# much simpler definition of a link as a function:
def Link(text, url):
    return '<a href="%s">%s</a>' % (url, text)

def link(text, url):
    return '<a href="%s">%s</a>' % (url, text)

def table(*args, **kwargs):
    'return HTML code for a table as a string. See Table class for parameters.'
    return str(Table(*args, **kwargs))

def calculate_scores():
    accuracy_dict = {
        "jessime": ["kimiko", "internet_player_1", "internet_player_3"],
        "kimiko": ["jessime", "wes", "sherif"],
        "wes": ["jessime", "kimiko", "internet_player_1"],
        "sherif": ["internet_player_1", "internet_player_3", "internet_player_3"],
    }

    game_data = {
            "funniest": ["jessime", "jessime", "kimiko", "kimiko"],
            "accuracy": accuracy_dict,
        }

    #########################3

    n_other_players = len(game_data.get('accuracy')) - 1

    all_lists = []

    for ls in accuracy_dict.values():
        all_lists.extend(ls)

    scores_list = []

    for player, player_votes in game_data.get('accuracy').items():
        #player_scores = [player]
        player_scores = []

        score_best = round(game_data.get('funniest').count(player)/n_other_players, 2)
        player_scores.append(score_best)

        score_accuracy = round(sum(1 for vote in player_votes if vote.startswith('internet_player'))/n_other_players, 2)
        player_scores.append(score_accuracy)

        score_deception = round(all_lists.count(player)/n_other_players, 2)
        player_scores.append(score_deception)

        score_overall = round(sum(player_scores), 2)
        player_scores.append(score_overall)

        player_scores.insert(0, player)
        scores_list.append(player_scores)

    scores_list = sorted(scores_list, key=lambda x: x[-1], reverse=True)

    scores_list.insert(0, ['player', 'best', 'accuracy', 'deception', 'overall'])
    my_table = table(scores_list).replace('\n', '')
    return scores_list, my_table
