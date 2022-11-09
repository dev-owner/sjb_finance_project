import json

import boto3
import OpenDartReader
from botocore.exceptions import ClientError


def get_secret():
    secret_name = "dart"
    region_name = "ap-northeast-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    return json.loads(get_secret_value_response['SecretString'])['api_key']



if __name__ == '__main__':


    ### 0. 객체 생성 ###
    # 객체 생성 (API KEY 지정)
    api_key = get_secret()
    print(api_key)

    dart = OpenDartReader(api_key)

    ### 1. 공시정보 ###

    # 특정기업(삼성전자) 특정 날짜 이후 공시목록 (날짜에 다양한 포맷이 가능합니다 2022, '2022-01-01', '20220101' )
    # print(dart.list('삼성전자', start='2022-11-01'))  # 2022-01-01 ~ 오늘


    # # ==== 1-3. 공시정보 - 공시서류원본파일 ====
    # # 삼성전자 사업보고서 (2022년 반기사업보고서) 원문 텍스트
    # xml_text = dart.document('20220816001711')
    # print(xml_text)
    #
    #
    # ### 3. 상장기업 재무정보 ###
    # # 상장법인(금융업 제외)의 주요계정과목(재무상태표, 손익계산서)
    #
    # # 삼성전자 2021 재무제표
    doc = dart.finstate('삼성전자', 2021)
    print(doc)
    #
    #
    # ### 4. 지분공시 ###
    # # 대량보유 상황보고 (종목코드, 종목명, 고유번호 모두 지정 가능)
    # print(dart.major_shareholders('삼성전자'))
