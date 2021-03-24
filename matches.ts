interface Match {
  localTeam: number;
  visitorTeam: number;
  localScore: number;
  visitorScore: number;
  date: Date;
  tournamentDate: number;
}

const matches5: Match[] = [
  {
    localTeam: 15,
    visitorTeam: 13,
    localScore: 0,
    visitorScore: 0,
    date: new Date(2021, 2, 19, 19, 0),
    tournamentDate: 5,
  },
  {
    localTeam: 12,
    visitorTeam: 10,
    localScore: 0,
    visitorScore: 0,
    date: new Date(2021, 2, 20, 13, 0),
    tournamentDate: 5,
  },
  {
    localTeam: 8,
    visitorTeam: 4,
    localScore: 2,
    visitorScore: 0,
    date: new Date(2021, 2, 20, 15, 30),
    tournamentDate: 5,
  },
  {
    localTeam: 9,
    visitorTeam: 3,
    localScore: 2,
    visitorScore: 2,
    date: new Date(2021, 2, 20, 18, 30),
    tournamentDate: 5,
  },
  {
    localTeam: 11,
    visitorTeam: 2,
    localScore: 1,
    visitorScore: 1,
    date: new Date(2021, 2, 21, 13, 0),
    tournamentDate: 5,
  },
  {
    localTeam: 7,
    visitorTeam: 16,
    localScore: 1,
    visitorScore: 2,
    date: new Date(2021, 2, 21, 15, 30),
    tournamentDate: 5,
  },
  {
    localTeam: 6,
    visitorTeam: 1,
    localScore: 0,
    visitorScore: 1,
    date: new Date(2021, 2, 21, 18, 0),
    tournamentDate: 5,
  },
  {
    localTeam: 5,
    visitorTeam: 14,
    localScore: 1,
    visitorScore: 0,
    date: new Date(2021, 2, 22, 19, 0),
    tournamentDate: 5,
  },
];

console.log(JSON.stringify(matches5));
