# -*- coding: cp936 -*-
from __future__ import print_function  
import sys
import os
from ctypes import *

# ���ؽӿڷ�Ŀ¼ http://www.yundama.com/apidoc/YDM_SDK.html
# ����������ѯ http://www.yundama.com/apidoc/YDM_ErrorCode.html
# ���к������ѯ http://www.yundama.com/apidoc

#print('>>>���ڳ�ʼ��...')

YDMApi = windll.LoadLibrary('D:/Python27/yzm/yundamaAPI-x64')

# 1. http://www.yundama.com/index/reg/developer ע�Ὺ�����˺�
# 2. http://www.yundama.com/developer/myapp ��������
# 3. ʹ����ӵ����ID����Կ���п��������ܷ��ֳ�

appId = 2957   # ����ɣģ������߷ֳɱ�Ҫ��������¼�����ߺ�̨���ҵ��������ã�
appKey = '5634ea89ff1717dfa14378f3c0fe76f8'     # �����Կ�������߷ֳɱ�Ҫ��������¼�����ߺ�̨���ҵ��������ã�

#print('����ɣģ�%d\r\n�����Կ��%s' % (appId, appKey))

# ע����������ͨ��Ա�˺ţ����ǿ������˺ţ�ע���ַ http://www.yundama.com/index/reg/user
# �����߿�����ϵ�ͷ���ȡ��ѵ������

#��ͨ�˺�
username = "weiwei2016"
password = "weijc7788"

####################### һ��ʶ���� YDM_EasyDecodeByPath #######################

#print('\r\n>>>����һ��ʶ��...')

# ����1004��ʾ4λ��ĸ���֣���ͬ�����շѲ�ͬ����׼ȷ��д������Ӱ��ʶ���ʡ��ڴ˲�ѯ�������� http://www.yundama.com/price.html
codetype = 3000

# ����30���ֽڴ��ʶ����
result = c_char_p("                              ")     

# ʶ��ʱʱ�� ��λ����
timeout = 60

# ��֤���ļ�·��
filename = 'D:/�ҵĽ�ѧ/Python/��������-����/12/douban123/yanzhengma/captcha.png'

# һ��ʶ������������� YDM_SetAppInfo �� YDM_Login���ʺϽű�����
captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)

#print("һ��ʶ����֤��ID��%d��ʶ������%s" % (captchaId, result))

################################################################################


########################## ��ͨʶ���� YDM_DecodeByPath #########################

#print('\r\n>>>���ڵ�½...')

# ��һ������ʼ���ƴ��룬ֻ�����һ�μ���
YDMApi.YDM_SetAppInfo(appId, appKey)

# �ڶ�������½�ƴ����˺ţ�ֻ�����һ�μ���
uid = YDMApi.YDM_Login(username, password)

if uid > 0:

    #print('>>>���ڻ�ȡ���...')
    
    # ��ѯ�˺�������Ҫ����
    balance = YDMApi.YDM_GetBalance(username, password)
    
    #print('��½�ɹ����û�����%s��ʣ����֣�%d' % (username, balance))

    #print('\r\n>>>������ͨʶ��...')

    # ����������ʼʶ��
    
    # ����1004��ʾ4λ��ĸ���֣���ͬ�����շѲ�ͬ����׼ȷ��д������Ӱ��ʶ���ʡ��ڴ˲�ѯ�������� http://www.yundama.com/price.html
    codetype = 3000

    # ����30���ֽڴ��ʶ����
    result = c_char_p("                              ")     

    # ��֤���ļ�·��
    filename = 'getimage.jpg'

    # ��ͨʶ���������ȵ��� YDM_SetAppInfo �� YDM_Login ��ʼ��
    captchaId = YDMApi.YDM_DecodeByPath(filename, codetype, result)

    #print("��ͨʶ����֤��ID��%d��ʶ������%s" % (captchaId, result.value))
    print(result.value,end='')
else:
	pass
    #print('��½ʧ�ܣ�������룺%d' % uid)

################################################################################

#print('\r\n>>>����������ѯ http://www.yundama.com/apidoc/YDM_ErrorCode.html')

#raw_input('\r\n������ɣ����س�������...')
