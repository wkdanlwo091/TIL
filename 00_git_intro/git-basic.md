# 마크다운(Mark Down)

# `마크다운(Mark Down)`



> 퍼스 빅데이터를 활용한 IOT 시스템 개발 ( Feat.)



## 1.문법

### 1.1 Header

> 헤더는 제목을 표현할 때 사용합니다.
>
> 것이 아니라 의미론적인 중요도를 가집니다.

- h1~h6 까지 표현이 가능합니다.
- #의 개수로 표현하거나 <h1> </h1> 형태로 표현 가능합니다.



### 1.2 List

<h1>하하하하</h1>

> 목록을 나열할 때 사용합니다.
>
> 순서가 필요한 항몪과 그렇지 않은 항목으로 구분할 수 있습니다.
>
> 순서/순서x 항목을 같이 사용할 수 있습니다.

<ul><li>하하</li></ul>



### 1.3 Code Block

> 코드 블럭은 작성한 코드를 작성하거나 강조하고 싶을 때 사용합니다. 
>
> 코드 블럭은 인라인과 블록 단위로 구분 할 수 있습니다. 

- Inline

  - 인라인으로 처리하고 싶은 부분을 `(백틱)으로 감싸줍니다

- Block

  -  (백틱)을 3번 입력하고  엔터를 눌러서 생성합니다. 

-  $git add. 

- git commit -m "commit message"

- git push origin master

  ```bash
  $git add.
  git commit -m "commit message"
  git push origin master
  ```

  ```html
  <a href > </a>
  ```

  

  

  ### 1.4 Image

> 로컬에 있는 이미지를 삽입하거나 이미지 링크를 활용합니다. 

 '![](data:image/png;base64,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)'를 작성하고 '()' 안에 주소를 입력합니다.

이때 [] 안에는 이미지 이름을 입력합니다. 

로컬에 있는 이미지 파일을 로드할 때는 절대경로가 아닌 상대경로를 사용합니다. 

* 하하하

![](C:\Users\wkdan\TIL\00_git_intro\images\git_img)

### Link

	> 
	>
	>  특정 주소로 링크를 걸 때 사용합니다.

[Markdown_tutorial](https://gist.github.com/ihoneymon/652be052a0727ad59601)를 작성하고 





### 1.6 Table

(파이프) 사이에 칼럼을 작성하고 엔터를 입력합니다.

마지막 컬럼을 작성하고 뒤에 '|'를 붙여줍니다. 





| Working Directory | Staging Area | Remote Repo |
| ----------------- | ------------ | ----------- |
|                   |              |             |

| 파이프 사이에 | 들어가는게 | 칼럼 네임 |      |      |
| ------------- | ---------- | --------- | ---- | ---- |
|               |            |           |      |      |
|               |            |           |      |      |
|               |            |           |      |      |
|               |            |           |      |      |



### 1.7 기타 

인용문

> 입력하고 엔터키를 누릅니다.
>
> git은 컴퓨터의 파일 변경 사항을 추적합니다.



* 중첩된 인용문을 사용할 수 있습니다.

* git add

  $git commit -m "first commit"

**수평선**

* ---, ***, '____' 를 입력하여 작성합니다. 

____

Working Directory

****

Staging Area

----

Remote Repository(Github)

---

**강조!**

* 이탤릭체는 해당 부분을 '*', _ 1개로 감싸줍니다.
* 보드체는 해당 부분을 ** , __ 2개로 감싸줍니다.
* __dd__ 
* 취소선은 '~~'개로 감싸줍니다.



*이것은 이탤릭체입니다.*

__이것은 보드체입니다.__

~~이것은 취소선입니다.~~

**Why so serious**



### Git

* Git 개념

  * git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다.

  ---

  

* Git 설정

  * 전역 영역설정 commit 기록의 주인을 등록

  * ```git
    * $git config --global username "username"
    * $git config --global user.email "wkdanlwo091@gmail.com"
    ```

  

* Git 기본

  * git init 해당 디렉토리를 Git이 관리하도록 초기화
  * add 파일명 커밋할 목록에 추가 
  * commit -m 커밋메시지(히스토리의 한 단위) 만들기
  * git push origin master 현재 까지의 역사(commit)가 기록되어 있는 곳에 
  * 새로 생성한 커밋 반영

* Git 저장소 

  * 로컬(Working directory) -staging area - remote repository(github, bitbucket, gitlab)
  * 로컬 컴퓨터 저장소 해당 버전의 스냅샷(기록), 원격 저장소

* Git branch

  * 같은 작업물을 기반으로 동ㅇ시에 다양한 작업을 할 수 있게 만들어 주는 
  * 기능
  * 독립적인 작업 영역 안에서 마음대로 소스코드를 변경 할 수 있다 . 분리된 작업 영역에서 변경된 내용은 추후에 기존 버전과 비교해서 새로운 하나의 버전을 만들어 낼 수 있다. 

![](./images/captured.png)

| 마크다운                                             | 깃헙                                                  |
| ---------------------------------------------------- | ----------------------------------------------------- |
| 마크다운은 Github의 Readme.md 를 작성 할때 사용한다. | 깃헙은 버젼관리 프로그램으로 깃을 모아둔 저장소 이다. |



### 하하하

> > >
> > >
> > >하하핳하



#### 하하하하

