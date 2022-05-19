DROP DATABASE IF EXISTS breaking_news_app;

CREATE DATABASE breaking_news_app;

\c breaking_news_app;

DROP TABLE IF EXISTS news;

CREATE TABLE news
(
  id SERIAL PRIMARY KEY,
  title text NOT NULL,
  author text NOT NULL,
  description text NOT NULL,
  image_url text
  
);

INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('No Ukraine breakthrough but NATO and Russia eye more talks', 
  'ABC News',
  'LORNE COOK Associated Press',
  'https://s.abcnews.com/images/International/WireAP_bde0a32b07a344b88aa0ad10811c7f24_16x9_992.jpg');

INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('This Early Symptom is One You Should Watch for With Omicron Infections Rising', '- NBC10 Boston','Staff and wire reports if you have been exposed to someone with COVID and are watching for symptoms what are some of the first signs you might be infected? With omicron cases rising','https://media.nbcboston.com/2022/01/GettyImages-1237641619.jpg?quality=85&strip=all&crop=0px%2C375px%2C4000px%2C2250px&resize=1200%2C675');

INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('The Nvidia Shield is getting Android 11 and other upgrades','- The Verge,Chaim Gartenberg', 'The Nvidia Shield set-top box keeps on trucking with its latest Shield Software Experience Upgrade 9.0, which adds Android 11 to the nearly seven-year-old hardware. It also adds a variety of other useful upgrades around Bluetooth and game streaming.', 'https://cdn.vox-cdn.com/thumbor/IazbpIF_CRG5qYsHWbPhCBBl-bg=/0x5:1280x675/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/23163583/SHIELD_TV_Experience_9.0_1280x680.jpg');

INSERT INTO news
  (title, author, description, image_url)
VALUES 
  ('U.S. Senate Democrats unveil Russia sanctions bill to bolster Ukraine', '- Reuters', 'U.S. Senate Democrats on Wednesday unveiled a bill to impose sweeping sanctions on top Russian government and military officials, including President Vladimir Putin, and key banking institutions if Moscow engages in hostilities against Ukraine.', 'https://www.reuters.com/resizer/TNtHOcIwjtyj9v_w7RLkH4uLgh4=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/34VQYDBORRMELNKNPKSRM6HGTA.jpg');

INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('What does Joe Judges termination mean for Giants QB Daniel Jones?', ' - Giants Wire, John Fennelly', 'With Dave Gettleman and Joe Judge gone, the future looks murky for New York Giants QB Daniel Jones, but dont close the door on him just yet.', 'https://giantswire.usatoday.com/wp-content/uploads/sites/67/2021/11/1356024763.jpg?w=1024&h=576&crop=1');

INSERT INTO news
  (title, author, description, image_url)
VALUES 
  ('Stock market news live updates: Stocks rise as investors eye inflation data, showing biggest jump since 1982 - Yahoo Finance', 'Emily McCormick', 'Stock futures rose Wednesday morning as investors eyed a new report on inflation, which showed another decades-high rate of price increases across the...', 'https://s.yimg.com/ny/api/res/1.2/KgKOYNqmhAgjnRAKcDbCNw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD04MDA-/https://s.yimg.com/os/creatr-uploaded-images/2022-01/7e6ba110-7330-11ec-95e2-662bcfb215f8');

INSERT INTO news
  (title, author, description, image_url)
VALUES  
  ('Some marijuana compounds can block coronavirus from entering cells: study - New York Post', 'Yaron Steinbuch', 'The researchers found that a pair of hemp compounds bind to the SARS-CoV-2 spike protein, blocking a vital step in the deadly bug’s path to infect people.', 'https://nypost.com/wp-content/uploads/sites/2/2022/01/cannabis-1.jpg?quality=90&strip=all&w=1024');

INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('Boris Johnson apologizes in Parliament over BYOB event during lockdown - The Washington Post', 'William Booth, Karla Adam', 'Johnson told irate lawmakers that they would have to await an internal inquiry before deciding whether the event broke the rules.', 'https://www.washingtonpost.com/wp-apps/imrs.php?src=https://d1i4t8bqe7zgj6.cloudfront.net/01-12-2022/t_39265e7980eb4be4bda64ca38c04feb3_name_8f910a6e_73a0_11ec_a26d_1c21c16b1c93_scaled.jpg&w=1440');

INSERT INTO news
  (title, author, description, image_url)
VALUES 
  ('Agent -- Safety Eric Weddle unretires, joins Los Angeles Rams for playoffs after Jordan Fuller injury', '- ESPN', 'Safety Eric Weddle is coming out of retirement to sign with the Rams for the playoffs, his agent announced Wednesday.', 'https://a.espncdn.com/combiner/i?img=%2Fphoto%2F2020%2F0206%2Fr662629_1296x729_16%2D9.jpg');


INSERT INTO news
  (title, author, description, image_url)
VALUES 
  ('Its not about the green bubbles, Apple - CNET', 'Mike Sorrentino', 'Commentary: Its about far more than group chats and emojis.', 'https://www.cnet.com/a/img/K52f0VeykTm9muh-dNUP0ggLLt4=/1200x630/2019/11/08/fb22b5a0-75a8-46e2-9247-b3eee66712d5/imessage-iphone-11-pro-max.jpg');


INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('Oldest Known Fossil of a Modern Human May Be Even More Ancient Than We Thought', '- Gizmodo,George Dvorsky', 'The revised estimate, based on nearby volcanic ash, fits in nicely with most models of modern human evolution.', 'https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/c3cb3c4160f617cd20e45b1d042fbb28.jpg');


INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('Earth Is Surrounded by 1,000-Light-Year Wide Bubble -Source of All Nearby',  'Young Stars - SciTechDaily', 'The Earth sits in a 1,000-light-year-wide void surrounded by thousands of young stars — but how did those stars form? In a paper appearing today (Janaury 12, 2022) in Nature, astronomers at the Center for Astrophysics | Harvard & Smithsonian (CfA) and the Spa…', 'https://scitechdaily.com/images/The-Local-Bubble-scaled.jpg');


INSERT INTO news
  (title, author, description, image_url)
VALUES 
  ('Judge rules sexual assault lawsuit against Prince Andrew can move ahead - CNN', 'Eric Levenson and Brian Vitagliano, CNN', 'A federal judge in New York denied a motion to dismiss a lawsuit against Prince Andrew filed by Virginia Giuffre, a woman who alleges she was sexually trafficked to the royal when she was underage.', 'https://cdn.cnn.com/cnnnext/dam/assets/190906152149-prince-andrew-guifre-maxwell-super-tease.jpg');


INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('Wordle clones yanked from Apples App Store - Polygon', 'Austen Goslin', 'World many clones have disappeared off of the Apple App Store. While a few copycat games remain, the ones that took the Wordle name all appear to be gone.', 'https://cdn.vox-cdn.com/thumbor/Vcey9yudBaLfKe8xpXgl8KPptwM=/0x0:1920x1005/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/23163381/wordle_photo.jpg');


INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('Cancer mortality rates continue to decline amid "major progress" in lung cancer early detection and treatment - CNN', 'Deidre McPhillips, CNN', 'Cancer mortality rates have been dropping for nearly two decades, aided by major progress in the early detection and treatment options for lung cancer, according to the American Cancer Societys annual report on cancer statistics, published Wednesday.', 'https://cdn.cnn.com/cnnnext/dam/assets/220112105611-lung-cancer-progress-annual-cancer-report-file-restricted-091316-super-tease.jpg');

INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('Fatal Philadelphia fire likely started with a lighter igniting a Christmas tree, fire commissioner says - CNN', 'Taylor Romine, CNN', 'Its a ""near certainty"" that a Philadelphia duplex fire that claimed 12 lives was started by a lighter igniting a Christmas tree on the second floor of the building, city Fire Commissioner Adam Thiel said Tuesday.', 'https://cdn.cnn.com/cnnnext/dam/assets/220107032159-philadelphia-fire-scene-file-01052022-super-tease.jpg');


INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('N.Y. Giants GM search: Breaking down the 9 candidates to replace Dave Gettleman - The Athletic', 'Dan Duggan','From former college and pro scouts to ex-Pro Bowl players, the Giants are considering a wide range of external candidates for the job.', 'https://cdn.theathletic.com/app/uploads/2022/01/12104401/GettyImages-1293332921-1024x683.jpeg');


INSERT INTO news
  (title, author, description, image_url)
VALUES
  ('West Virginia Gov. Jim Justice says he is extremely unwell after testing positive for coronavirus - The Washington Post', 'Timothy Bella', 'Justice, who is vaccinated and boosted, said in a news release that while he was surprised he tested positive, the GOP governor was thankful to the Lord above that I have been vaccinated, I have been boosted, and that I have an incredible support system, espec…', 'https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/ASJRWDDP6II6ZMPCAU45VD2EKE.jpg&w=1440');
  