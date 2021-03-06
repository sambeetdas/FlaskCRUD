USE [College]
GO
/****** Object:  Table [dbo].[Student]    Script Date: 5/25/2020 10:28:57 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Student](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nchar](10) NULL,
	[PhoneNumber] [nchar](10) NULL,
 CONSTRAINT [PK_Student] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[User]    Script Date: 5/25/2020 10:28:57 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[User](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Username] [nchar](10) NULL,
	[Password] [nchar](10) NULL,
 CONSTRAINT [PK_User] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  StoredProcedure [dbo].[Delete_Data]    Script Date: 5/25/2020 10:28:57 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[Delete_Data] 

@ID int

AS
BEGIN

	SET NOCOUNT ON;

	BEGIN TRANSACTION;   
		DELETE FROM STUDENT WHERE ID = @ID 
	COMMIT TRANSACTION; 

	select 'Id is Deleted' as Info
END
GO
/****** Object:  StoredProcedure [dbo].[Get_All_Data]    Script Date: 5/25/2020 10:28:57 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[Get_All_Data] 

AS
BEGIN

	SET NOCOUNT ON;

   SELECT Id ,Name ,PhoneNumber FROM Student
END
GO
/****** Object:  StoredProcedure [dbo].[Get_Data_By_Id]    Script Date: 5/25/2020 10:28:57 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

Create PROCEDURE [dbo].[Get_Data_By_Id] 

@ID int

AS
BEGIN

	SET NOCOUNT ON;

   SELECT Id ,Name ,PhoneNumber FROM Student where Id = @ID
END
GO
/****** Object:  StoredProcedure [dbo].[Insert_Data]    Script Date: 5/25/2020 10:28:57 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[Insert_Data] 
	@NAME NCHAR(10),
	@PHONENUMBER NCHAR(10)
AS
BEGIN

	SET NOCOUNT ON;
	SET IMPLICIT_TRANSACTIONS OFF;

	BEGIN TRANSACTION;   
		INSERT INTO STUDENT  VALUES (@NAME, @PHONENUMBER)
	COMMIT TRANSACTION; 

	SELECT Id ,Name ,PhoneNumber FROM Student where Id = @@IDENTITY

END
GO
/****** Object:  StoredProcedure [dbo].[Update_Data]    Script Date: 5/25/2020 10:28:57 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[Update_Data] 

@NAME nchar(10),
@PHONENUMBER nchar(10),
@ID int

AS
BEGIN

	SET NOCOUNT ON;

	BEGIN TRANSACTION;   
		   UPDATE STUDENT  SET PHONENUMBER = @PHONENUMBER, NAME = @NAME	WHERE ID = @ID
	COMMIT TRANSACTION; 

	SELECT Id ,Name ,PhoneNumber FROM Student where Id = @ID
END
GO
/****** Object:  StoredProcedure [dbo].[Valid_User]    Script Date: 5/25/2020 10:28:57 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[Valid_User] 
	@USERNAME NCHAR(10),
	@PASSWORD NCHAR(10)
AS
BEGIN

	SET NOCOUNT ON;

    SELECT COUNT(1) as Count FROM [USER] WHERE USERNAME = @USERNAME AND PASSWORD = @PASSWORD
END
GO
