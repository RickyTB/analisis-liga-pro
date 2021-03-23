interface Match {
  localTeam: number;
  visitorTeam: number;  
  localScore: number;
  visitorScore: number;
  date: Date,
  tournamentDate: number;
}

const matches1: Match[] = [
  {
    localTeam: 9,
    visitorTeam: 12,
    localScore: 1,
    visitorScore: 1,
    date: new Date(2019, 1, 8, 20, 0),
    tournamentDate: 1,
  },
  {
    localTeam: 8,
    visitorTeam: 4,
    localScore: 0,
    visitorScore: 2,
    date: new Date(2019, 1, 9, 15, 0),
    tournamentDate: 1,
  },
  {
    localTeam: 11,
    visitorTeam: 14,
    localScore: 3,
    visitorScore: 2,
    date: new Date(2019, 1, 9, 17, 15),
    tournamentDate: 1,
  },
  {
    localTeam: 3,
    visitorTeam: 6,
    localScore: 5,
    visitorScore: 2,
    date: new Date(2019, 1, 9, 19, 30),
    tournamentDate: 1,
  },
  {
    localTeam: 5,
    visitorTeam: 10,
    localScore: 3,
    visitorScore: 2,
    date: new Date(2019, 1, 10, 14, 0),
    tournamentDate: 1,
  },
  {
    localTeam: 2,
    visitorTeam: 7,
    localScore: 0,
    visitorScore: 2,
    date: new Date(2019, 1, 10, 16, 5),
    tournamentDate: 1,
  },
  {
    localTeam: 15,
    visitorTeam: 16,
    localScore: 1,
    visitorScore: 2,
    date: new Date(2019, 1, 10, 18, 0),
    tournamentDate: 1,
  },
  {
    localTeam: 1,
    visitorTeam: 13,
    localScore: 0,
    visitorScore: 1,
    date: new Date(2019, 1, 11, 19, 15),
    tournamentDate: 1,
  },
];

console.log(JSON.stringify(matches1));