# 登録

### 物理名:register

|項目名|物理名|データ型|主キー|インデックス|外部キー参照|NULL許可|備考|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|登録ID|app_id|数値|○|-|-|-||
|登録No|app_no|文字列|-|○|-|-||
|登録日|app_date|-|-|-|-|-||
|ステータス|status_cd|数値|-|-|[状態.状態コード](status.md)|-||
|適用開始日時|start_at|タイムスタンプ|-|-|-|-|default:"2000-01-01 00:00:00"|
|適用終了日時|end_at|タイムスタンプ|-|-|-|-|default:"2999-12-31 23:59:59"|
|論理削除フラグ|is_delete|真偽値|-|-|-|-|true:削除データ default:false|
|作成者|create_user|数値|-|-|ユーザーマスタ.ユーザーID|○||
|作成日時|create_at|タイムスタンプ|-|-|-|-||
|更新者|update_user|数値|-|-|ユーザーマスタ.ユーザーID|○||
|更新日時|update_at|タイムスタンプ|-|-|-|-||
