# 部署マスタ

#### 物理名: m_department

|項目名|物理名|データ型|主キー|インデックス|外部キー参照|NULL許可|備考|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|部署コード|department_cd|数値|○|-|-|-||
|部署名|department_name|文字型|-|-|-|-||
|適用開始日時|start_at|タイムスタンプ|-|-|-|-|default:"2000-01-01 00:00:00"|
|適用終了日時|end_at|タイムスタンプ|-|-|-|-|default:"2999-12-31 23:59:59"|
|論理削除フラグ|is_delete|真偽値|-|-|-|-|true:削除データ default:false|
|作成者|create_user|数値|-|-|ユーザーマスタ.ユーザーID|○||
|作成日時|create_at|タイムスタンプ|-|-|-|-||
|更新者|update_user|数値|-|-|ユーザーマスタ.ユーザーID|○||
|更新日時|update_at|タイムスタンプ|-|-|-|-||

##### マスタデータ
|ブランドカテゴリコード|ブランドカテゴリ名称|
|:--:|:--:|
|100|営業部|
|101|経理部|
|102|総務部|
|103|人事部|
|104|マーケティング部|
|105|システム部|
|106|研究部|
|107|法務部|
|108|広報部|