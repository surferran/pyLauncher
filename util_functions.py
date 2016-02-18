# general file that includes all kind of funcitions i want to use in my App

from myImports import *
##

MY_DEBUG = not(True)
# MY_DEBUG = (True)

# definitions
myGlobal_CONSTANTS = {}
myGlobal_CONSTANTS['USER_PATH']     =  './USER_data/'
myGlobal_CONSTANTS['USER_FILE']     =  'user_list.csv'

# functions / methods :
def get_user_file_rel():
    return myGlobal_CONSTANTS['USER_PATH'] + myGlobal_CONSTANTS['USER_FILE']

######################################################
def load_user_list():
    f_name = get_user_file_rel()
    table = pd.read_table(f_name , sep='\t')
    if MY_DEBUG :
        print table
        # my buttons info will be :
        # (should be basic 5 parameters. others are just TABs for inner ident)
        print table.values
        for line in table.values:
            print "line len : " + str(len(line))
            print line
            # num of first 'nan' :
            pd.isnull(line).sum(axis=0)
            pd.isnull(line).sum(axis=0).tolist()
    ###############
    levels,deep = get_user_hirarchy(table.values)
    ###############
    # complete and set the indexes of each line
    user_pref_dictionary    = {}
    user_pref_dictionary['item index']      = []
    user_pref_dictionary['name']            = []
    user_pref_dictionary['display type']    = []
    user_pref_dictionary['image file']      = []
    user_pref_dictionary['size in pixels']  = []
    user_pref_dictionary['scaling']         = []
    # build :
    levels_indeces          = []
    for i in range(deep):
        levels_indeces.append(0)    # init counters for each indent level
    lines_indeces = list(levels) # init result by copy
    for l_ind, line in enumerate(table.values):
        for i in range(deep):
            if levels[l_ind] == 1.0/(10**i):   # ==pow(10,i)
                levels_indeces[i]       += 1
                lines_indeces[l_ind]     = levels_indeces[i]*levels[l_ind]
                if i>0:
                    lines_indeces[l_ind]    += levels_indeces[i-1]      # add to previous higher level last counter
                break
        if l_ind>0 :
            if levels[l_ind] > levels[l_ind-1]:  # zero lower level counter when back to the higher level
                levels_indeces[i+1]  = 0

        # continue and set the elemnts themselves
        start_index = i + 1
        user_pref_dictionary['item index']      .append(lines_indeces[l_ind])
        user_pref_dictionary['name']            .append(line[start_index])
        user_pref_dictionary['display type']    .append(line[start_index+1])
        user_pref_dictionary['image file']      .append(line[start_index+2])
        user_pref_dictionary['size in pixels']  .append(line[start_index+3])
        user_pref_dictionary['scaling']         .append(line[start_index+4])

        ele=dict_to_xml('ran_dict', user_pref_dictionary)
        print ele.text
        pass

    if MY_DEBUG :
        print user_pref_dictionary

    return user_pref_dictionary

###############     ###############
def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

# just 1st indication for each line level-deep (identification)
def get_user_hirarchy(lines):
    indeces = []
    max_deep_level = 1
    for line_index , line in enumerate(lines):
        line_mult  = 1.0
        deep_level = 1
        for inline_index, line_item in enumerate(line):
            isNan = pd.isnull(line_item)
            if inline_index == 0:
                continue
            # if inline_index > 1:
            if isNan:
                line_mult  /= 10
                deep_level += 1
                continue
            indeces.append(line_mult)
            max_deep_level = max(max_deep_level , deep_level)
            break
    return indeces ,max_deep_level
######################################################

def register_my_HotKey(item):  # item should be wx.Frame
    # do at caller : self.Bind(wx.EVT_HOTKEY, self.handleHotKey, id=self.hotKeyId)
    # This function registers the hotkey Alt+F1 with id=100
    item.hotKeyId = 100
    item.RegisterHotKey(
         item.hotKeyId,     # a unique ID for this hotkey
         win32con.MOD_ALT,  # the modifier key
         win32con.VK_F1)    # the key to watch for

if __name__ == '__main__':
    # test1 = get_user_file_rel()
    test2 = load_user_list()
    print test2
    print ' end testing '
    pass