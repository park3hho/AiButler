import bcrypt


class AuthFunction:
    @staticmethod
    def set_password(password: str) -> str:
        """
        주어진 일반 텍스트 비밀번호를 해싱합니다.
        """
        # bcrypt.hashpw는 바이트 문자열을 입력으로 받으므로 .encode('utf-8')을 사용합니다.
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        # 저장하기 위해 다시 문자열로 디코딩합니다.
        return hashed_password.decode("utf-8")

    @staticmethod
    def verify_password(plain_password: str, hashed_password_from_db: str) -> bool:
        """
        일반 텍스트 비밀번호와 데이터베이스에 저장된 해싱된 비밀번호를 비교합니다.
        """
        # bcrypt.checkpw는 일반 비밀번호와 해싱된 비밀번호 모두 바이트 문자열을 입력으로 받습니다.
        # 여기서 plain_password와 hashed_password_from_db는 이미 문자열이므로,
        # 각각 .encode('utf-8')을 사용하여 바이트로 변환합니다.
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), hashed_password_from_db.encode("utf-8")
        )
