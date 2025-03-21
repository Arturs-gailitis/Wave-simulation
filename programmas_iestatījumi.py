def iestatījumi(root, x_ass, y_ass):

    izmērs = str(x_ass) + 'x' + str(y_ass)

    root.geometry(izmērs)

    root.title('Programmas par viļņu zīmēšanu galvenā izvelne')

    root.config()

def programmas_beigas(root):

    root.destroy()