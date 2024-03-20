# API一覧

|API名|メソッド|URL|画面|呼出タイミング|概要|
|:--:|:--:|:--:|:--:|:--:|:--:|
|[ユーザー情報取得](./GET/Users.md)|GET|/user|-|ログイン時|ログインユーザーのユーザー情報取得|
|[ホーム情報取得](./GET/Home.md)|GET|/home|ホーム画面|ホーム画面表示時|ホーム画面に表示する内容を取得|
|[部署マスタ取得](./GET/Department.md)|GET|/department|一覧画面|画面表示字|部署マスタのデータをすべて取得|
|[担当者取得](.GET/AppUser.md)|GET|/app-user|一覧画面|画面表示字|部署マスタのデータをすべて取得|
|[支払いマスタ取得](./GET/Payment.md)|GET|/payment||||
|[サービスマスタ取得](./GET/Service.md)|GET|/service||||
|[業種業態マスタ取得](./GET/Industry.md)|GET|/industry||||
|[端末マスタ取得](./GET/Terminal.md)|GET|/terminal||||
|[ブランドマスタ取得](./GET/Brand.md)|GET|/brand||||
|[申請理由マスタ取得](./GET/Reason.md)|GET|/reason||||
|[ステータス取得](./GET/Status.md)|GET|/status||||
|[申請一覧情報取得](./GET/List.md)|GET|/list?status={status_cd}|一覧画面|一覧画面表示時|一覧に表示するリストを取得|
|[申請データ登録](./POST/Register.md)|POST|/app/{app_id}|入力画面|申請押下時|データを作成|
|[申請データ更新](./POST/Update.md)|POST|/app-save/{app_id}|入力画面|申請押下時|データを作成|
|[申請データ一時保存](./POST/TempSaved.md)|POST|/app-save|入力画面|押下時|データを作成|
|[申請データ削除](./POST/Delete.md)|DELETE|/app/{app_id}|入力画面|押下時|データを作成|
|[取下げAPI](./POST/Withdraw.md)|POST|/app-drop/{app_id}|申請詳細画面|取下げボタン押下時|データを作成|
