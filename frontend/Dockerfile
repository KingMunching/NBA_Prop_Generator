# frontend/Dockerfile
FROM node:20

WORKDIR /app

# Copy package files first
COPY package*.json ./

# Install all deps
RUN npm install

# Copy the rest of your frontend code
COPY . .

# Expose Vite’s port
EXPOSE 5173

# Run Vite dev server
CMD ["npm", "run", "dev"]
