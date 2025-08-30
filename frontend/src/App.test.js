import { render, screen } from '@testing-library/react';
import App from './App';

test('renders main heading', () => {
  render(<App />);
  const heading = screen.getByText(/Coachy Services/i);
  expect(heading).toBeInTheDocument();
});
