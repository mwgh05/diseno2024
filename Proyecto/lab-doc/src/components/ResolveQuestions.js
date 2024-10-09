import React from 'react';
import './styles/ResolveQuestions.css';

const ResolveQuestions = ({ question, onSubmit }) => {
  const [answer, setAnswer] = React.useState('');

  const handleSubmit = () => {
    onSubmit(answer);
  };

  return (
    <div className="resolve-questions">
      <h2>Resolve Question</h2>
      <p>{question}</p>
      <input
        type="text"
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
      />
      <button onClick={handleSubmit}>Submit Answer</button>
    </div>
  );
};

export default ResolveQuestions;
